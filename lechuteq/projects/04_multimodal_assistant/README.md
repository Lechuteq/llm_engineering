# 04 — Multimodal AI Assistant (Text + Image + Audio)

## 🇬🇧 English

**Goal:** A single AI agent that combines text chat, image generation (DALL-E 3), and text-to-speech audio. When the user asks about a destination city, the assistant:
1. Looks up the price (SQLite tool call)
2. Generates a vacation-style pop-art image
3. Speaks the reply aloud

**Custom UI:** `gr.Blocks` layout with chatbot + image + audio panels side-by-side.

**Origin:** Week 2 Day 5.

**Tech stack:** Python 3.12, `openai` (chat + DALL-E 3 + TTS), `Pillow`, `base64`, `sqlite3`, `gradio.Blocks`.

**Run:**
```bash
uv run python multimodal_assistant.py
# Auto-opens browser to Gradio UI
```

**Try asking:**
- "How much to fly to Sydney?"
- "Tell me about a trip to Tokyo"

> ⚠️ **Cost warning:** DALL-E 3 image generation is ~$0.04 per call, TTS is ~$0.015 per 1K characters. Use sparingly during testing.

---

## 🇵🇱 Polski

**Cel:** Pojedynczy agent AI łączący czat tekstowy, generowanie obrazów (DALL-E 3) i syntezę mowy. Gdy użytkownik pyta o miasto docelowe, asystent:
1. Sprawdza cenę (wywołanie narzędzia SQLite)
2. Generuje wakacyjny obraz w stylu pop-art
3. Wypowiada odpowiedź na głos

**Niestandardowy UI:** Layout `gr.Blocks` z chatbotem + obrazem + audio obok siebie.

**Pochodzenie:** Tydzień 2 Dzień 5.

**Stack technologiczny:** Python 3.12, `openai` (chat + DALL-E 3 + TTS), `Pillow`, `base64`, `sqlite3`, `gradio.Blocks`.

**Uruchomienie:**
```bash
uv run python multimodal_assistant.py
# Automatycznie otwiera przeglądarkę z UI Gradio
```

**Spróbuj zapytać:**
- "Ile kosztuje lot do Sydney?"
- "Opowiedz o podróży do Tokio"

> ⚠️ **Uwaga na koszty:** Generowanie obrazu DALL-E 3 to ~$0.04 za wywołanie, TTS to ~$0.015 za 1K znaków. Używaj oszczędnie podczas testów.
