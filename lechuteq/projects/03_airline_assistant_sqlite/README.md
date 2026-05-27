# 03 — Airline AI Assistant (SQLite Edition)

## 🇬🇧 English

**Goal:** AI customer support assistant for an airline ("FlightAI") with real database-backed tool calling. Customer asks about prices; LLM autonomously decides when to call `get_ticket_price` or `set_ticket_price`.

**Custom upgrade:** Replaced course's in-memory Python `dict` with **SQLite database** (`prices.db`) for persistent state — production-style pattern.

**Tools exposed to LLM:**
- `get_ticket_price(destination_city)` — query
- `set_ticket_price(city, price)` — admin upsert (custom homework)

**Multi-tool dispatch:** Handles multiple tool calls in a single LLM response (advanced pattern).

**Origin:** Week 2 Day 4 + Lechuteq SQLite enhancement.

**Tech stack:** Python 3.12, `openai` (tool calling), `sqlite3`, `gradio.ChatInterface`, JSON Schema.

**Run:**
```bash
uv run python airline_assistant.py
# Opens Gradio UI at http://127.0.0.1:7860
```

**Try asking:**
- "How much is a ticket to Tokyo?"
- "Set the price for Berlin to 599"
- "What about Warsaw?"

---

## 🇵🇱 Polski

**Cel:** AI asystent obsługi klienta linii lotniczej ("FlightAI") z wywoływaniem narzędzi opartym na prawdziwej bazie danych. Klient pyta o ceny; LLM autonomicznie decyduje, kiedy wywołać `get_ticket_price` lub `set_ticket_price`.

**Własne ulepszenie:** Zastąpiono kursowy słownik in-memory **bazą SQLite** (`prices.db`) dla trwałego stanu — wzorzec produkcyjny.

**Narzędzia dostępne dla LLM:**
- `get_ticket_price(destination_city)` — zapytanie
- `set_ticket_price(city, price)` — admin upsert (własna praca domowa)

**Dispatch wielu narzędzi:** Obsługuje wiele wywołań narzędzi w jednej odpowiedzi LLM (zaawansowany wzorzec).

**Pochodzenie:** Tydzień 2 Dzień 4 + ulepszenie SQLite od Lechuteq.

**Stack technologiczny:** Python 3.12, `openai` (tool calling), `sqlite3`, `gradio.ChatInterface`, JSON Schema.

**Uruchomienie:**
```bash
uv run python airline_assistant.py
# Otwiera UI Gradio pod http://127.0.0.1:7860
```

**Spróbuj zapytać:**
- "Ile kosztuje bilet do Tokyo?"
- "Ustaw cenę do Berlina na 599"
- "A do Warszawy?"
