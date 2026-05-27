# 02 — Company Brochure Generator

## 🇬🇧 English

**Goal:** Given just a company name and URL, automatically discover relevant pages (About, Careers, Products) and produce a markdown sales brochure.

**Architecture:**
1. **Link curator** (`gpt-5-nano`) — picks relevant pages from raw href list, returns structured JSON
2. **Brochure assembler** (`gpt-4.1-mini`) — combines pages into one prompt, streams markdown brochure

**Origin:** Week 1 Day 5.

**Tech stack:** Python 3.12, `openai` (structured JSON + streaming), `beautifulsoup4`.

**Run:**
```bash
# Demo (HuggingFace)
uv run python brochure_generator.py

# Custom company
uv run python brochure_generator.py "Anthropic" "https://anthropic.com"
```

---

## 🇵🇱 Polski

**Cel:** Mając tylko nazwę firmy i URL, automatycznie wykrywać istotne strony (O nas, Kariera, Produkty) i wygenerować broszurę sprzedażową w markdown.

**Architektura:**
1. **Kurator linków** (`gpt-5-nano`) — wybiera istotne strony z listy href, zwraca ustrukturyzowany JSON
2. **Składacz broszury** (`gpt-4.1-mini`) — łączy strony w jeden prompt, strumieniuje broszurę markdown

**Pochodzenie:** Tydzień 1 Dzień 5.

**Stack technologiczny:** Python 3.12, `openai` (ustrukturyzowany JSON + streaming), `beautifulsoup4`.

**Uruchomienie:**
```bash
# Demo (HuggingFace)
uv run python brochure_generator.py

# Własna firma
uv run python brochure_generator.py "Anthropic" "https://anthropic.com"
```
