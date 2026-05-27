"""Airline AI Customer Support Assistant with SQLite-backed tool calling.

Custom enhancement: Replaced the course's in-memory dict with a real SQLite
database for ticket prices, demonstrating production-style tool calling.

Tools:
- get_ticket_price(destination_city) → reads from prices.db
- set_ticket_price(city, price) → upserts into prices.db (custom homework)

Origin: Week 2 Day 4, with SQLite upgrade by Lechuteq.
"""

import json
import os
import sqlite3
import sys
from pathlib import Path

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI


MODEL = "gpt-4.1-mini"
DB = str(Path(__file__).parent / "prices.db")

SYSTEM_MESSAGE = """
You are a helpful assistant for an Airline called FlightAI.
Give short, courteous answers, no more than 1 sentence.
Always be accurate. If you don't know the answer, say so.
You have access to tools that can look up ticket prices and update them.
"""


# ─── DATABASE ──────────────────────────────────────────────────────────────


def init_db():
    """Create the prices table and seed it with sample data."""
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
    print(f"DATABASE TOOL CALLED: Getting price for {city}", flush=True)
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT price FROM prices WHERE city = ?", (city.lower(),))
        result = cursor.fetchone()
        if result:
            return f"Ticket price to {city} is ${result[0]}"
        return f"No price data available for {city}"


def set_ticket_price(city: str, price: float) -> str:
    print(f"DATABASE TOOL CALLED: Setting price for {city} to ${price}", flush=True)
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO prices (city, price) VALUES (?, ?) "
            "ON CONFLICT(city) DO UPDATE SET price = ?",
            (city.lower(), price, price),
        )
        conn.commit()
    return f"Price for {city} set to ${price}"


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

set_price_function = {
    "name": "set_ticket_price",
    "description": "Set the price of a return ticket to the destination city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "The city for which to set the price"},
            "price": {"type": "number", "description": "The new price of the ticket"},
        },
        "required": ["city", "price"],
        "additionalProperties": False,
    },
}

TOOLS = [
    {"type": "function", "function": price_function},
    {"type": "function", "function": set_price_function},
]


# ─── TOOL DISPATCH ─────────────────────────────────────────────────────────


def handle_tool_calls(message) -> list[dict]:
    responses = []
    for tool_call in message.tool_calls:
        args = json.loads(tool_call.function.arguments)
        name = tool_call.function.name

        if name == "get_ticket_price":
            content = get_ticket_price(args["destination_city"])
        elif name == "set_ticket_price":
            content = set_ticket_price(args["city"], args["price"])
        else:
            content = f"Unknown tool: {name}"

        responses.append({
            "role": "tool",
            "content": content,
            "tool_call_id": tool_call.id,
        })
    return responses


# ─── CHAT LOOP ─────────────────────────────────────────────────────────────


def chat(message: str, history: list, client: OpenAI) -> str:
    history = [{"role": h["role"], "content": h["content"]} for h in history]
    messages = (
        [{"role": "system", "content": SYSTEM_MESSAGE}]
        + history
        + [{"role": "user", "content": message}]
    )

    response = client.chat.completions.create(
        model=MODEL, messages=messages, tools=TOOLS
    )

    while response.choices[0].finish_reason == "tool_calls":
        msg = response.choices[0].message
        tool_responses = handle_tool_calls(msg)
        messages.append(msg)
        messages.extend(tool_responses)
        response = client.chat.completions.create(
            model=MODEL, messages=messages, tools=TOOLS
        )

    return response.choices[0].message.content


# ─── ENTRY POINT ───────────────────────────────────────────────────────────


def main():
    load_dotenv(override=True)
    if not os.getenv("OPENAI_API_KEY"):
        sys.exit("Error: OPENAI_API_KEY not set in environment")

    init_db()
    client = OpenAI()

    def chat_callback(message, history):
        return chat(message, history, client)

    print("Launching FlightAI Customer Support (SQLite edition)...")
    gr.ChatInterface(fn=chat_callback, type="messages").launch()


if __name__ == "__main__":
    main()
