# Lechuteq — Portfolio Projects

Standalone, runnable Python projects extracted from the LLM Engineering course notebooks.
Each project lives in its own folder with a `README.md` and a runnable entry-point script.

---

## 🇬🇧 English

### 📂 Project Index

| # | Project | Week/Day | Showcase Skills |
|---|---------|----------|-----------------|
| [01](./01_polish_sme_analyzer/) | Polish SME Business Analyzer | W1D1 (custom) | Polish prompting, business analysis |
| [02](./02_brochure_generator/) | Company Brochure Generator | W1D5 | Multi-step LLM pipeline, JSON output, streaming |
| [03](./03_airline_assistant_sqlite/) | Airline AI (SQLite) | W2D4 (custom) | Tool calling, real database backend, Gradio |
| [04](./04_multimodal_assistant/) | Multimodal Assistant | W2D5 | DALL-E 3, TTS, gr.Blocks custom UI |

### 📁 Folder Structure

```
lechuteq/projects/
├── README.md                         # This file
├── common/
│   └── scraper.py                    # Shared web scraping helper
├── 01_polish_sme_analyzer/
│   ├── sme_analyzer.py
│   └── README.md
├── 02_brochure_generator/
│   ├── brochure_generator.py
│   └── README.md
├── 03_airline_assistant_sqlite/
│   ├── airline_assistant.py
│   └── README.md
└── 04_multimodal_assistant/
    ├── multimodal_assistant.py
    ├── image_Sydney.webp             # DALL-E 3 generated artifact
    ├── image_Warsaw.webp             # DALL-E 3 generated artifact
    └── README.md
```

### ⚙️ Setup

All projects share the parent repo's `.venv` and dependencies. From repo root:

```bash
uv sync
```

API keys are read from the repo-level `.env` file (already configured).

### 🚀 Running Any Project

```bash
# From the project's folder
cd lechuteq/projects/03_airline_assistant_sqlite
uv run python airline_assistant.py
```

Or use the full path:

```bash
# From anywhere
uv run python lechuteq/projects/02_brochure_generator/brochure_generator.py "Anthropic" "https://anthropic.com"
```

### 💡 Design Notes

- **Why standalone `.py` files instead of notebooks?** Portfolio code should be runnable from a terminal, importable, and testable. Notebooks are great for exploration, but `.py` files show production readiness.
- **Why a shared `common/scraper.py`?** Multiple projects need web scraping; DRY (Don't Repeat Yourself).
- **Why SQLite over in-memory dicts?** Persistence, transactional safety, and a real-world data layer story.
- **Why bilingual READMEs?** This is a personal portfolio — written for both English-speaking recruiters and Polish-speaking peers.

---

## 🇵🇱 Polski

### 📂 Indeks projektów

| # | Projekt | Tydz./Dzień | Pokazywane umiejętności |
|---|---------|-------------|-------------------------|
| [01](./01_polish_sme_analyzer/) | Polski analizator MŚP | T1D1 (własne) | Polskie prompty, analiza biznesowa |
| [02](./02_brochure_generator/) | Generator broszury firmowej | T1D5 | Wieloetapowy pipeline LLM, JSON, streaming |
| [03](./03_airline_assistant_sqlite/) | Asystent linii lotniczej (SQLite) | T2D4 (własne) | Tool calling, prawdziwa baza danych, Gradio |
| [04](./04_multimodal_assistant/) | Multimodalny asystent | T2D5 | DALL-E 3, TTS, własny UI gr.Blocks |

### ⚙️ Konfiguracja

Wszystkie projekty używają wspólnego `.venv` i zależności z repozytorium nadrzędnego. Z katalogu głównego:

```bash
uv sync
```

Klucze API są odczytywane z pliku `.env` na poziomie repozytorium (już skonfigurowane).

### 🚀 Uruchomienie dowolnego projektu

```bash
# Z folderu projektu
cd lechuteq/projects/03_airline_assistant_sqlite
uv run python airline_assistant.py
```

Lub używając pełnej ścieżki:

```bash
# Z dowolnego miejsca
uv run python lechuteq/projects/02_brochure_generator/brochure_generator.py "Anthropic" "https://anthropic.com"
```

### 💡 Decyzje projektowe

- **Dlaczego samodzielne pliki `.py` zamiast notatników?** Kod portfolio powinien być uruchamialny z terminala, importowalny i testowalny. Notebooki są świetne do eksploracji, ale pliki `.py` pokazują gotowość produkcyjną.
- **Dlaczego wspólny `common/scraper.py`?** Wiele projektów potrzebuje web scrapingu; DRY (Don't Repeat Yourself).
- **Dlaczego SQLite zamiast słowników in-memory?** Trwałość, bezpieczeństwo transakcyjne i prawdziwa historia warstwy danych.
- **Dlaczego dwujęzyczne READMI?** To osobiste portfolio — pisane zarówno dla anglojęzycznych rekruterów, jak i polskojęzycznych kolegów.

---

### 🔗 Related Documents

- [`../LECHUTEQ_README.md`](../LECHUTEQ_README.md) — Full course progress documentation (EN + PL)
- [`../../CLAUDE.md`](../../CLAUDE.md) — Guidance for Claude Code working in this repo
- [`../../README.md`](../../README.md) — Ed Donner's original course README
