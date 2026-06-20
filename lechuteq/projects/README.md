# Lechuteq — Portfolio Projects

Standalone, runnable Python projects extracted from the LLM Engineering course notebooks.
Weeks 1–2 projects live in their own folders with a `README.md` and a runnable entry-point script.
Weeks 3–8 projects are documented here and linked to their source notebooks in the course tree.

---

## English

### Project Index

| # | Project | Week/Day | What was built | Showcase Skills |
|---|---------|----------|---------------|-----------------|
| [01](./01_polish_sme_analyzer/) | Polish SME Business Analyzer | W1D1 (custom) | Web scraper + OpenAI prompt for EU SME analysis in Polish | Polish prompting, business analysis, BeautifulSoup |
| [02](./02_brochure_generator/) | Company Brochure Generator | W1D5 | Two-step LLM pipeline: link curation + brochure assembly with streaming | Multi-step pipeline, JSON structured output, streaming |
| [03](./03_airline_assistant_sqlite/) | Airline AI Assistant (SQLite) | W2D4 (custom) | Airline chatbot with SQLite price database and full tool calling | Tool calling, real database backend, Gradio |
| [04](./04_multimodal_assistant/) | Multimodal AI Assistant | W2D5 | Chat + DALL-E 3 image gen + TTS audio in one custom Gradio UI | DALL-E 3, TTS, gr.Blocks, multi-tool agent |
| 05 | Meeting Minutes Generator | W3D5 | Audio file → Whisper transcription → Llama structured meeting minutes | Whisper ASR, Llama 3.2-3B, 4-bit quantization, HuggingFace |
| 06 | Python → C++ / Rust Code Generator | W4D3–5 | Translates Python to compiled languages via frontier LLMs, compiles and benchmarks | Multi-provider LLM, subprocess, Gradio, 9-model benchmark |
| 07 | InsureLLM Expert Knowledge Worker | W5D1–5 | Full RAG chatbot from keyword lookup to semantic chunking + reranking + query rewriting | LangChain, ChromaDB, all-MiniLM-L6-v2, reranking, query rewriting |
| 08 | Amazon Product Price Predictor | W6D1–5 | ML pipeline on 820k products: XGBoost, PyTorch DNN, OpenAI fine-tuning | scikit-learn, XGBoost, PyTorch, OpenAI fine-tuning, Groq Batch API |
| 09 | Llama 3.2-3B QLoRA Fine-tuned Pricer | W7D1–5 | Fine-tuned 3B model on 400k items, beats GPT-5.1 (39.85 vs 44.74 RMSE) | QLoRA, SFTTrainer, bitsandbytes, W&B, HuggingFace Hub |
| 10 | "The Price is Right" — Agentic System | W8D1–5 | Autonomous multi-agent: scans deals, prices them, pushes phone notifications | Modal.com, multi-agent orchestration, ChromaDB RAG, Pushover, Gradio |

---

### Standalone Projects (Weeks 1–2)

These are extracted into runnable `.py` files:

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

---

### Notebook-Based Projects (Weeks 3–8)

---

#### Project 05 — Meeting Minutes Generator
**Source:** `week3/Week 3 Day 5 - Meeting Minutes product.ipynb`
**Platform:** Google Colab (T4 GPU)

End-to-end audio-to-document pipeline. Takes a real city council meeting recording (Denver, MP3), transcribes it with either open-source Whisper or the OpenAI Whisper API, then feeds the transcript into Llama 3.2-3B (4-bit quantized) to produce structured meeting minutes with summary, key points, takeaways, and action items.

**Stack:** `transformers` (Whisper + Llama), `openai` (Whisper API), `BitsAndBytesConfig`, Google Colab Drive mount.

---

#### Project 06 — Python to C++ / Rust Code Generator
**Source:** `week4/day3.ipynb`, `week4/day4.ipynb`, `week4/day5.ipynb`
**Platform:** Local (Ubuntu 24.04, i5-14600K)

Translates Python into high-performance C++ or Rust using frontier LLMs, compiles the output natively, and benchmarks the speedup. Includes a Gradio UI with a model dropdown for interactive use.

**C++ benchmark results (pi calculation, 200M iterations, Python baseline ~19s):**

| Place | Model | Speedup |
|-------|-------|---------|
| 1st | Gemini 2.5 Pro | ~1,440x |
| 2nd | Grok 4 | ~1,060x |
| 3rd | GPT-5 | ~233x |
| 4th | Claude Sonnet 4.5 | ~184x |

**Rust benchmark results (harder LCG max-subarray, most models failed):**

| Place | Model | Speedup |
|-------|-------|---------|
| 1st | OpenAI gpt-oss-120B | ~110,000x |
| 2nd | Grok 4 | ~106,000x |
| 3rd | gpt-oss-20B | ~99,000x |

**Stack:** `openai`, `anthropic`, `subprocess` (compile + run), `system_info.py`, `gradio`, `styles.py`.

---

#### Project 07 — InsureLLM Expert Knowledge Worker (RAG)
**Source:** `week5/day1.ipynb` through `week5/day5.ipynb`

Full RAG system built in five progressive iterations over a fictional insurance tech company knowledge base (employee profiles, product sheets, contracts):

1. Keyword-based retrieval (baseline)
2. LangChain + ChromaDB vector store + t-SNE visualization
3. LangChain RAG pipeline + Gradio chatbot
4. LLM-judge evaluation framework (accuracy / completeness / relevance)
5. Advanced RAG: LLM-driven semantic chunking + reranking + query rewriting

The Day 5 version is production-grade: the full pipeline rewrites the query before retrieval, re-ranks retrieved chunks by relevance, then generates the answer — all without LangChain abstractions.

**Stack:** `langchain`, `langchain-chroma`, `langchain-huggingface`, `chromadb`, `sentence-transformers` (`all-MiniLM-L6-v2`), `openai`, `pydantic`, `sklearn` (t-SNE), `plotly`.

---

#### Project 08 — Amazon Product Price Predictor
**Source:** `week6/day1.ipynb` through `week6/day5.ipynb`

Full ML pipeline from raw data to fine-tuned model on 820,000 Amazon product descriptions across 8 categories.

**Progression of models built:**

| Model | RMSE |
|-------|------|
| Constant baseline | 106.18 |
| Linear Regression | 101.56 |
| Random Forest | 72.28 |
| XGBoost | 68.23 |
| PyTorch Neural Network (2 epochs) | 63.97 |
| OpenAI fine-tuned GPT-4.1-nano (20k examples) | 67.75 |
| Deep Neural Network (5 epochs, 800k items) | 46.49 |
| GPT-5.1 (zero-shot, best frontier) | 44.74 |

**Stack:** `datasets` (HuggingFace), `scikit-learn`, `xgboost`, `torch`, `openai` (Files + Fine-tuning API), `groq` (Batch API), `litellm`, `wandb`.

---

#### Project 09 — QLoRA Fine-tuned Llama 3.2-3B Price Predictor
**Source:** `week7/day1.ipynb` through `week7/day5.ipynb`
**Platform:** Google Colab (T4 for Lite, A100 for Full)

Fine-tuned Meta Llama 3.2-3B on 400,000 Amazon product descriptions using QLoRA (4-bit NF4 quantization + low-rank adapters). Full mode trained for 3 epochs on A100.

**Result: 39.85 RMSE — beats GPT-5.1 (44.74 RMSE)**

A 3-billion-parameter open source model, domain-fine-tuned, outperforms a trillion-parameter frontier model on this task. This is the headline result of the entire course.

**Stack:** `transformers`, `trl` (`SFTTrainer`), `peft` (`LoraConfig`, `PeftModel`), `bitsandbytes`, `wandb`, HuggingFace Hub.

---

#### Project 10 — "The Price is Right" Autonomous Multi-Agent System
**Source:** `week8/day1.ipynb` through `week8/day5.ipynb`, `week8/agents/`, `week8/price_is_right.py`

Fully autonomous agent system that scans the internet for product deals, estimates their true value using three parallel AI strategies, and pushes phone notifications when it finds a real bargain.

**Agent architecture:**

```
AutonomousPlanningAgent (LLM-driven tool-calling loop)
├── ScannerAgent       — scrapes deal sites, GPT filters top 5 structured deals
├── EnsembleAgent      — weighted pricing (80% / 10% / 10%)
│   ├── FrontierAgent      — ChromaDB RAG over 400k products + GPT-5.1
│   ├── SpecialistAgent    — fine-tuned Llama deployed on Modal.com (serverless GPU)
│   └── NeuralNetworkAgent — deep neural network from Week 6
└── MessagingAgent     — Pushover push notifications to phone
```

Deployed as a standalone Gradio application (`price_is_right.py`) that runs indefinitely, persisting discovered deals in `memory.json`.

**Stack:** `modal` (cloud GPU deployment), `chromadb`, `sentence-transformers`, `openai` (tool calling + structured output), `requests` (Pushover API), `gradio` (`gr.Blocks`, `gr.Timer`), `litellm`.

---

### Setup

All projects share the parent repo's `.venv` and dependencies. From repo root:

```bash
uv sync
```

API keys are read from the repo-level `.env` file.

### Running Standalone Projects (01–04)

```bash
cd lechuteq/projects/03_airline_assistant_sqlite
uv run python airline_assistant.py
```

### Running Week 8 Standalone App

```bash
uv run python week8/price_is_right.py
```

---

### Design Notes

- **Why standalone `.py` files for weeks 1–2?** Portfolio code should be runnable from a terminal and importable. Notebooks are for exploration; `.py` files show production readiness.
- **Why document weeks 3–8 here without extracting them?** Week 3–8 projects depend on GPU cloud (Colab, Modal), large datasets, or deployed services — they are not meant to run as local scripts. The notebooks are the canonical source.
- **Why SQLite over in-memory dicts?** Persistence, transactional safety, and a real-world data layer story.
- **Why bilingual READMEs?** Personal portfolio — written for both English-speaking readers and Polish-speaking peers.

---

## Polski

### Indeks projektów

| # | Projekt | Tydz./Dzień | Co zostało zbudowane | Pokazywane umiejętnosci |
|---|---------|-------------|----------------------|------------------------|
| [01](./01_polish_sme_analyzer/) | Polski analizator MŚP | T1D1 (własne) | Web scraper + prompt OpenAI do analizy MŚP wg UE po polsku | Polskie prompty, analiza biznesowa |
| [02](./02_brochure_generator/) | Generator broszury firmowej | T1D5 | Dwuetapowy pipeline LLM: kurator linków + skład broszury ze streamingiem | Wieloetapowy pipeline, strukturalny JSON, streaming |
| [03](./03_airline_assistant_sqlite/) | Asystent linii lotniczej (SQLite) | T2D4 (własne) | Chatbot z bazą SQLite i pełnym wywoływaniem narzędzi | Tool calling, prawdziwa baza danych, Gradio |
| [04](./04_multimodal_assistant/) | Multimodalny asystent AI | T2D5 | Czat + generowanie obrazów DALL-E 3 + TTS w jednym UI Gradio | DALL-E 3, TTS, gr.Blocks, agent wielonarzędziowy |
| 05 | Generator protokołów ze spotkań | T3D5 | Plik audio → transkrypcja Whisper → protokół Llama 3.2-3B | Whisper ASR, Llama 3.2-3B, kwantyzacja 4-bit, HuggingFace |
| 06 | Generator kodu Python → C++ / Rust | T4D3–5 | Tłumaczy Python na skompilowane języki, kompiluje i benchmarkuje | Multi-provider LLM, subprocess, Gradio, benchmark 9 modeli |
| 07 | Ekspert wiedzy InsureLLM (RAG) | T5D1–5 | Pełny chatbot RAG: od słownika do semantycznego chunkingu + rerankingu | LangChain, ChromaDB, all-MiniLM-L6-v2, reranking, przepisywanie zapytań |
| 08 | Predyktor cen produktów Amazon | T6D1–5 | Pipeline ML na 820k produktach: XGBoost, PyTorch DNN, fine-tuning OpenAI | scikit-learn, XGBoost, PyTorch, fine-tuning OpenAI, Groq Batch API |
| 09 | Llama 3.2-3B QLoRA (fine-tuned) | T7D1–5 | 3B model fine-tuned na 400k elementach, bije GPT-5.1 (39,85 vs 44,74 RMSE) | QLoRA, SFTTrainer, bitsandbytes, W&B, HuggingFace Hub |
| 10 | "The Price is Right" — System agentyczny | T8D1–5 | Autonomiczny multi-agent: skanuje okazje, wycenia, wysyła powiadomienia na telefon | Modal.com, orchestracja agentów, RAG ChromaDB, Pushover, Gradio |

---

### Dokumenty powiązane

- [`../LECHUTEQ_README.md`](../LECHUTEQ_README.md) — Pełna dokumentacja postępów kursu (EN + PL)
- [`../../CLAUDE.md`](../../CLAUDE.md) — Wytyczne dla Claude Code w tym repo
- [`../../README.md`](../../README.md) — Oryginalny README kursu Ed Donnera
