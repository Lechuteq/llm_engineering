"""Multimodal Airline AI Assistant — Text + Image (DALL-E 3) + Audio (TTS).

When the user asks about a destination city:
1. LLM calls get_ticket_price tool (SQLite backend)
2. Generates a vacation-style pop-art image via DALL-E 3
3. Speaks the response aloud via gpt-4o-mini-tts

Custom UI: gr.Blocks with chat + image + audio panels side-by-side.

Origin: Week 2 Day 5.
"""

import base64
import json
import os
import sqlite3
import sys
from io import BytesIO
from pathlib import Path

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
from PIL import Image


MODEL = "gpt-4.1-mini"
IMAGE_MODEL = "dall-e-3"
TTS_MODEL = "gpt-4o-mini-tts"
TTS_VOICE = "onyx"

DB = str(Path(__file__).parent / "prices.db")

SYSTEM_MESSAGE = """
You are a helpful assistant for an Airline called FlightAI.
Give short, courteous answers, no more than 1 sentence.
Always be accurate. If you don't know the answer, say so.
"""


# ─── DATABASE ──────────────────────────────────────────────────────────────


def init_db():
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS prices (city TEXT PRIMARY KEY, price REAL)"
        )
        seed = {"london": 799, "paris": 899, "tokyo": 1420, "sydney": 2999, "warsaw": 199}
        for city, price in seed.items():
            cursor.execute(
                "INSERT INTO prices (city, price) VALUES (?, ?) "
                "ON CONFLICT(city) DO NOTHING",
                (city, price),
            )
        conn.commit()


def get_ticket_price(city: str) -> str:
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT price FROM prices WHERE city = ?", (city.lower(),))
        result = cursor.fetchone()
        if result:
            return f"Ticket price to {city} is ${result[0]}"
        return f"No price data available for {city}"


# ─── MULTIMODAL HELPERS ────────────────────────────────────────────────────


def artist(client: OpenAI, city: str) -> Image.Image:
    """Generate a vacation pop-art image for a city using DALL-E 3."""
    image_response = client.images.generate(
        model=IMAGE_MODEL,
        prompt=(
            f"An image representing a vacation in {city}, showing tourist spots "
            f"and everything unique about {city}, in a vibrant pop-art style"
        ),
        size="1024x1024",
        n=1,
        response_format="b64_json",
    )
    image_data = base64.b64decode(image_response.data[0].b64_json)
    return Image.open(BytesIO(image_data))


def talker(client: OpenAI, message: str) -> bytes:
    """Convert text to audio via TTS."""
    response = client.audio.speech.create(
        model=TTS_MODEL,
        voice=TTS_VOICE,
        input=message,
    )
    return response.content


# ─── TOOL DEFINITIONS ──────────────────────────────────────────────────────

price_function = {
    "name": "get_ticket_price",
    "description": "Get the price of a return ticket to the destination city.",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city that the customer wants to travel to",
            },
        },
        "required": ["destination_city"],
        "additionalProperties": False,
    },
}

TOOLS = [{"type": "function", "function": price_function}]


def handle_tool_calls_and_return_cities(message) -> tuple[list[dict], list[str]]:
    responses = []
    cities = []
    for tool_call in message.tool_calls:
        if tool_call.function.name == "get_ticket_price":
            args = json.loads(tool_call.function.arguments)
            city = args["destination_city"]
            cities.append(city)
            responses.append({
                "role": "tool",
                "content": get_ticket_price(city),
                "tool_call_id": tool_call.id,
            })
    return responses, cities


# ─── CHAT LOOP ─────────────────────────────────────────────────────────────


def chat(history: list, client: OpenAI):
    history = [{"role": h["role"], "content": h["content"]} for h in history]
    messages = [{"role": "system", "content": SYSTEM_MESSAGE}] + history
    response = client.chat.completions.create(
        model=MODEL, messages=messages, tools=TOOLS
    )
    cities: list[str] = []
    image = None

    while response.choices[0].finish_reason == "tool_calls":
        msg = response.choices[0].message
        tool_responses, new_cities = handle_tool_calls_and_return_cities(msg)
        cities.extend(new_cities)
        messages.append(msg)
        messages.extend(tool_responses)
        response = client.chat.completions.create(
            model=MODEL, messages=messages, tools=TOOLS
        )

    reply = response.choices[0].message.content
    history += [{"role": "assistant", "content": reply}]

    voice = talker(client, reply)
    if cities:
        image = artist(client, cities[0])

    return history, voice, image


# ─── GRADIO UI ─────────────────────────────────────────────────────────────


def build_ui(client: OpenAI):
    def chat_callback(history):
        return chat(history, client)

    def put_message_in_chatbot(message, history):
        return "", history + [{"role": "user", "content": message}]

    with gr.Blocks(title="FlightAI Multimodal Assistant") as ui:
        gr.Markdown("# ✈️ FlightAI — Multimodal AI Assistant")
        gr.Markdown("_Ask about flights — get prices, vacation images, and voice replies_")

        with gr.Row():
            chatbot = gr.Chatbot(height=500, type="messages")
            image_output = gr.Image(height=500, interactive=False, label="Destination")
        with gr.Row():
            audio_output = gr.Audio(autoplay=True, label="Voice reply")
        with gr.Row():
            message = gr.Textbox(label="Chat with our AI Assistant:")

        message.submit(
            put_message_in_chatbot,
            inputs=[message, chatbot],
            outputs=[message, chatbot],
        ).then(
            chat_callback,
            inputs=chatbot,
            outputs=[chatbot, audio_output, image_output],
        )

    return ui


def main():
    load_dotenv(override=True)
    if not os.getenv("OPENAI_API_KEY"):
        sys.exit("Error: OPENAI_API_KEY not set in environment")

    init_db()
    client = OpenAI()
    ui = build_ui(client)
    ui.launch(inbrowser=True)


if __name__ == "__main__":
    main()
