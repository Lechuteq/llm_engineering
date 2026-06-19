# LECHUTEQ — LLM Engineering Course Progress

> **GitHub:** [github.com/Lechuteq/llm_engineering](https://github.com/Lechuteq/llm_engineering)
> **Author of course:** Ed Donner ([ed-donner/llm_engineering](https://github.com/ed-donner/llm_engineering))
> **Student:** Lesław Nowakowski (Lechuteq)
> **Period:** November 2025 – May 2026 (ongoing)

---

## Sync Status Notice (2026-06-19)

**Reported progress:** 6 of 8 weeks completed.
**Synced to GitHub:** Weeks 1, 2, 3 (Week 3 Colab notebooks uploaded 2026-06-19).
**Missing from this machine:** Weeks 4, 5, 6 work.

The portfolio in [`projects/`](./projects/) reflects Weeks 1 and 2 currently.

**Likely locations of missing work (to check at home):**
- 🏠 Home Windows 11 machine — local clone never pushed
- 🏠 Home Ubuntu machine — different local clone never pushed
- ☁️ Google Colab — check `colab.research.google.com → File → Recent notebooks`
- 📄 Loose `.ipynb` files in Downloads / Documents folders

**Search commands:**
```bash
# Linux / macOS / WSL
find / -name "day*.ipynb" -path "*week[4-8]*" 2>/dev/null

# Windows PowerShell
Get-ChildItem -Path C:\ -Recurse -Filter "day*.ipynb" -ErrorAction SilentlyContinue |
  Where-Object { $_.FullName -match "week[4-8]" }
```

**Next steps once found:** Drop them in `week4/`, `week5/`, etc., commit + push to origin, and extend the portfolio with projects `05_`, `06_`, … accordingly.

---

## 🇬🇧 ENGLISH VERSION

### 📋 Progress Overview

| Week | Day | Status | Topic |
|------|-----|--------|-------|
| 1 | 1 | ✅ Done (synced) | Website Summarizer (OpenAI) |
| 1 | 2 | ✅ Done (synced) | Multi-provider APIs + Ollama |
| 1 | 4 | ✅ Done (synced) | (Modified) |
| 1 | 5 | ✅ Done (synced) | Company Brochure Generator |
| 2 | 1 | ✅ Done (synced) | Frontier Models Comparison |
| 2 | 2 | ✅ Done (synced) | Gradio UIs |
| 2 | 3 | ✅ Done (synced) | Conversational AI Chatbot |
| 2 | 4 | ✅ Done (synced) | Airline AI with Tools (SQLite) |
| 2 | 5 | ✅ Done (synced) | Multimodal AI Assistant |
| 3 | 1 | ✅ Done (synced) | Colab + GPU Setup + Image Generation (diffusers) |
| 3 | 2 | ✅ Done (synced) | HuggingFace Pipelines (high-level API) |
| 3 | 3 | ✅ Done (synced) | Tokenizers deep-dive |
| 3 | 4 | ✅ Done (synced) | Models lower-level API + 4-bit quantization |
| 3 | 5 | ✅ Done (synced) | Meeting Minutes product (Audio → Whisper → Llama) |
| 4 | 1-5 | 🔍 Done elsewhere — needs sync | Code Generation |
| 5 | 1-5 | 🔍 Done elsewhere — needs sync | RAG (Retrieval Augmented Generation) |
| 6 | 1-5 | 🔍 Done elsewhere — needs sync | Fine-tuning |
| 7 | - | ⏳ Pending | Advanced Fine-tuning (Colab GPU) |
| 8 | - | ⏳ Pending | Agentic AI |

---

### 🗂️ WEEK 1 — Foundations of LLM API Usage

#### Day 1: Website Summarizer with OpenAI
**Goal:** First exposure to the OpenAI Chat Completions API by building a tool that scrapes a website and returns a markdown summary.

**What was built:**
- Web scraper using `BeautifulSoup` (via `scraper.py` helper)
- System prompt + user prompt design for "snarky" summaries
- Calls to OpenAI `gpt-4.1-mini` for summarization
- Display markdown output inside Jupyter via `IPython.display`
- **Custom homework extension:** A Polish-language business analysis prompt designed to evaluate SMEs (małe i średnie przedsiębiorstwa) according to EU definitions, identifying market segment, products vs. services, target audience, and comparing them with competitors.

**Tech stack:** Python, `openai`, `beautifulsoup4`, `requests`, `python-dotenv`, `IPython`, Jupyter Lab.

---

#### Day 2: Multi-Provider Frontier Models + Ollama (Local)
**Goal:** Explore Chat Completions endpoints across providers (OpenAI, Anthropic, Google, DeepSeek, Groq) and learn that they share an OpenAI-compatible structure. Also run a local model via Ollama.

**What was built:**
- Side-by-side calls to multiple LLM providers using the unified OpenAI client interface
- Comparison of reasoning effort levels on `gpt-5-nano` and `gpt-5-mini`
- Tested "hard puzzle" reasoning (a Pushkin bookshelf riddle)
- **Custom homework:** Refactored the Day 1 website summarizer to run locally with Ollama (`llama3.2`), proving the workflow runs entirely offline/free.

**Tech stack:** `openai`, `anthropic`, `google-generativeai`, `ollama`, `requests`.

---

#### Day 5: Company Brochure Generator (Multi-Page Web Analysis)
**Goal:** Build a full business product — given just a company name + URL, automatically discover relevant pages (About, Careers, Products) and produce a sales brochure.

**What was built:**
- Two-step LLM pipeline:
  1. **Link curator** — feeds raw page links into `gpt-5-nano` and asks for relevant links in structured JSON.
  2. **Brochure assembler** — combines landing page + selected pages into a single prompt and generates a markdown brochure.
- Streaming output for "typewriter-style" UX
- Manual testing with `huggingface.co` and `edwarddonner.com`

**Tech stack:** `openai` (structured JSON output), `beautifulsoup4`, streaming responses, Jupyter `update_display` for live rendering.

**Note:** Significant refactoring — the original notebook was 1351 lines; final size is 403 lines (clean and consolidated).

---

### 🗂️ WEEK 2 — Building User-Facing AI Products

#### Day 1: Comparing Frontier Models
**Goal:** Programmatically compare frontier models on simple questions, riddles, and reasoning tasks.

**What was built:**
- Unified client setup for OpenAI, Anthropic, Google, DeepSeek, Groq
- A/B testing prompts ("tell a joke for an LLM Engineering student", probability puzzles, classical reasoning)
- Tested various `reasoning_effort` levels (minimal / low / medium / high)
- 70 cells of explorations comparing model outputs

**Tech stack:** `openai`, `anthropic`, `google-generativeai`, `groq`, `litellm` patterns.

---

#### Day 2: Gradio User Interfaces
**Goal:** Wrap LLM functionality in beautiful, shareable web UIs using Gradio.

**What was built:**
- Simple `gr.Interface` callbacks (`fn=...`)
- Adding authentication to Gradio apps (`auth=(user, password)`)
- Dark mode forcing
- Generator-based streaming UIs with `yield`
- A Gradio version of the **company brochure generator** from Week 1 Day 5

**Tech stack:** `gradio>=5.49`, async generators, environment-based config.

---

#### Day 3: Conversational AI (Chatbot)
**Goal:** Build a stateful chat assistant using `gr.ChatInterface` with history awareness.

**What was built:**
- The `chat(message, history)` callback pattern
- Iterative refinement: pass-through bot → echo bot → real LLM responses → with system prompt
- "Clothes store assistant" persona with promotional logic (hats 60% off, items 50% off)
- One-shot prompting examples to anchor model behaviour

**Tech stack:** `gradio`, `openai`, system-prompt engineering.

---

#### Day 4: Airline AI Assistant with Tool Calling (SQLite!)
**Goal:** Use OpenAI's tool calling (function calling) to give the LLM access to a real backend.

**What was built:**
- **Custom enhancement:** Migrated the ticket prices from in-memory dictionary to **SQLite database** (`prices.db`) — a significant improvement over the course default!
- Tool function: `get_ticket_price(city)` with proper JSON Schema definition
- Handler for **multiple tool calls in a single response** (advanced pattern)
- Sequential tool-call handling (one after another)
- **Custom homework:** Added a price-setting tool (`set_ticket_price`) — meets the day's exercise spec

**Tech stack:** `openai` tool calling, `sqlite3`, `gradio.ChatInterface`, JSON Schema.

---

#### Day 5: Multimodal AI Assistant (Vision + Audio)
**Goal:** Combine text, image generation (DALL-E 3), audio (text-to-speech), and tool calls in one agent.

**What was built:**
- DALL-E 3 image generator (`artist(city)`) — produces vacation pop-art images for tool-detected cities
- TTS audio with `gpt-4o-mini-tts` (voice: onyx)
- A `gr.Blocks` custom UI layout with Chatbot + Image output + Audio output side-by-side
- Tool flow that captures cities mentioned and generates images dynamically
- **Custom artifacts:** `image_Sydney.webp`, `image_Warsaw.webp` — generated images saved as proof of the assistant working

**Tech stack:** `openai` (chat + images + audio), `Pillow`, `base64`, `pydub`, `gradio.Blocks`.

---

### 🗂️ WEEK 3 — Open Source Models, HuggingFace & Google Colab

All Week 3 notebooks ran on **Google Colab** with a free Tesla T4 GPU (16 GB VRAM). HuggingFace `HF_TOKEN` was provided via Colab Secrets.

---

#### Day 1: Google Colab Setup + Generative Image Models
**Goal:** First exposure to Google Colab as a GPU cloud environment, and running state-of-the-art image diffusion models without any local hardware.

**What was built:**
- GPU check via `nvidia-smi` confirming Tesla T4 connection
- HuggingFace login with `HF_TOKEN` from Colab Secrets
- Image generation with **SDXL-Turbo** (`stabilityai/sdxl-turbo`) — fast 4-step diffusion
- Image generation with **Stable Diffusion XL Base 1.0** (`stabilityai/stable-diffusion-xl-base-1.0`)
- **Two-model pipeline:** SDXL Base + SDXL Refiner chained together for higher quality
- Text-to-speech synthesis with `microsoft/speecht5_tts` + speaker embeddings from CMU Arctic dataset
- Showcase of **FLUX.1-schnell** (`black-forest-labs/FLUX.1-schnell`) running on a premium A100 GPU (paid tier demo with cost estimation: ~$0.015/run)

**Tech stack:** `diffusers`, `transformers`, `torch`, `datasets`, `soundfile`, `huggingface_hub`, Colab T4 GPU.

---

#### Day 2: HuggingFace Pipelines (High-Level Inference API)
**Goal:** Master the `pipeline()` abstraction from HuggingFace — one unified API for a dozen different AI tasks.

**What was built / explored:**
- **Sentiment analysis** — default model + `nlptown/bert-base-multilingual-uncased-sentiment` (5-star output)
- **Named Entity Recognition (NER)** — identifies persons, orgs, locations
- **Question answering** — extractive QA with context
- **Text summarization** — abstractive summarization
- **Translation** — EN→FR (default), EN→ES (`Helsinki-NLP/opus-mt-en-es`)
- **Zero-shot classification** — text categorized into arbitrary labels without training
- **Text generation** — GPT-2 style open-ended generation
- **Image generation** — SDXL-Turbo via `AutoPipelineForText2Image`
- **Audio (TTS)** — speecht5_tts via pipeline

**Custom Lechuteq additions (cells 20–21):**
- Personal SDXL prompt: *"A warm-dressed cyclist in a black ski jacket riding an orange-black mountain bike in snowy/frosty evening weather, heading to a white cottage office — vibrant pop-art style"*
- Second personal prompt: *"Python robot extracting data from PDF documents next to office worker — dark pop-art style"*

**Tech stack:** `transformers.pipeline`, `diffusers`, `datasets`, `soundfile`, `torch`.

---

#### Day 3: Tokenizers Deep-Dive
**Goal:** Understand what actually happens between your Python `messages=[]` dict and the raw text that enters a model — the crucial "aha moment" of the whole course.

**What was explored:**
- `AutoTokenizer` loaded for **Meta Llama 3.1-8B**
- `tokenizer.encode()` / `decode()` / `batch_decode()` — encoding text to token IDs and back
- Vocabulary size (`len(tokenizer.vocab)` = 128,000 for Llama)
- **Instruct variants** — `Meta-Llama-3.1-8B-Instruct` uses a chat template
- `tokenizer.apply_chat_template(messages)` — shows the real string that model sees (system/user/assistant tags)
- **Cross-model tokenizer comparison** across:
  - Llama 3.1 (Meta) — BPE vocabulary
  - Phi-4 Mini (`microsoft/Phi-4-mini-instruct`)
  - DeepSeek V3.1 (`deepseek-ai/DeepSeek-V3.1`)
  - QwenCoder 2.5 (`Qwen/Qwen2.5-Coder-7B-Instruct`) — code-specific tokenization (tokens per symbol)
- Each model has different chat template format — key insight for prompt engineering

**Tech stack:** `transformers.AutoTokenizer`, HuggingFace Hub, CPU (no GPU needed).

---

#### Day 4: Models — Lower-Level Transformer API
**Goal:** Go below the `pipeline()` abstraction and use `AutoModelForCausalLM` directly with tokenization, quantization, and streaming.

**What was built:**
- **4-bit quantization** with `BitsAndBytesConfig` (`load_in_4bit=True`, `bnb_4bit_quant_type="nf4"`, double quant) — fits large models into T4's 16 GB
- Loading **Llama 3.2-1B-Instruct** / **Llama 3.1-8B-Instruct** with `device_map="auto"` + quant config
- Memory footprint reporting: `model.get_memory_footprint()` — verified 4-bit compressed size
- Inspecting the raw **PyTorch model object** (layers, attention heads, MLP blocks)
- `model.generate(inputs, max_new_tokens=80)` — raw token generation
- `TextStreamer` for streaming token-by-token output
- Reusable `generate(model, messages, quant, max_new_tokens)` helper function
- Tested multiple models: **Phi** (Microsoft), **Gemma** (Google), **Qwen** (Alibaba), **DeepSeek**
- Memory cleanup: `del model, inputs; gc.collect(); torch.cuda.empty_cache()`

**Tech stack:** `transformers` (`AutoModelForCausalLM`, `AutoTokenizer`, `TextStreamer`, `BitsAndBytesConfig`), `torch`, `bitsandbytes`, `accelerate`.

---

#### Day 5: Meeting Minutes Product (Audio → Transcription → Structured Report)
**Goal:** Build a real end-to-end product combining audio transcription + LLM text generation — a "meeting minutes" generator.

**What was built:**
- Google Drive mount (`drive.mount("/content/drive")`) to access `denver_extract.mp3` (Denver City Council meeting audio)
- **Step 1 — Transcription** (two options compared):
  - Option A — Open source: `openai/whisper-medium.en` via HuggingFace pipeline (automatic speech recognition with timestamps)
  - Option B — Commercial: OpenAI `gpt-4o-mini-transcribe` API
  - Side-by-side comparison of both transcription outputs
- **Step 2 — Meeting Minutes Generation:**
  - System prompt designed to produce structured minutes: summary, key discussion points, takeaways, action items with owners
  - Used `meta-llama/Llama-3.2-3B-Instruct` with 4-bit quantization + `TextStreamer`
  - Output rendered in Markdown via `IPython.display`

**Tech stack:** `transformers` (Whisper ASR + Llama), `openai` (Whisper API), `BitsAndBytesConfig`, `google.colab.drive`, `IPython.display`.

---

### 🛠️ Common Tech Stack (Across All Weeks)

| Category | Libraries |
|----------|-----------|
| LLM SDKs | `openai`, `anthropic`, `google-generativeai`, `groq` |
| Local LLM | `ollama` (llama3.2), HuggingFace `transformers` |
| Open Source Models | Llama 3.1/3.2, Phi-4, Gemma, Qwen, DeepSeek, Whisper |
| Image Generation | `diffusers` (SDXL-Turbo, SDXL Base+Refiner, FLUX.1-schnell) |
| Speech | `microsoft/speecht5_tts`, `openai/whisper-medium.en`, `gpt-4o-mini-tts` |
| Quantization | `bitsandbytes` (4-bit NF4), `accelerate` |
| UI | `gradio>=5.49` |
| Web scraping | `beautifulsoup4`, `requests` |
| Data | `sqlite3` (custom upgrade!), `datasets==3.6.0` |
| Display | `IPython.display`, Markdown streaming |
| Media | `Pillow`, `base64`, `pydub`, `soundfile` |
| Cloud | Google Colab (T4 GPU free tier, A100 paid) |
| Env | `python-dotenv`, Colab Secrets (`userdata.get`) |
| Runtime | Python 3.12, Jupyter Lab 4.5, UV package manager |

---

### 💡 Tips for Future Weeks (3–8)

Building on what you've already done, here's how to make the upcoming projects shine:

#### 1. **Reuse Your Patterns**
You've already mastered:
- Streaming responses → keep using `yield` in Gradio for any long-running task
- Tool calling with SQLite → in Week 5 (RAG), you can swap the SQLite tool for a vector store query
- `gr.Blocks` layout → use this for all complex UIs in Weeks 4–8

#### 2. **Week 3 — HuggingFace & Open Source Models (Colab) ✅ DONE**
- You built the full progression: pipelines → tokenizers → raw models → real product
- **Key pattern to reuse:** The `generate(model, messages, quant, max_new_tokens)` helper from Day 4 is the standard way to run any HuggingFace causal model — copy it to Week 7 fine-tuning
- **Quantization matters:** 4-bit NF4 (`BitsAndBytesConfig`) lets 8B-parameter models fit in a T4's 16 GB — always use it on Colab free tier
- **Whisper vs. commercial:** You compared both transcription options — for production use gpt-4o-mini-transcribe (cleaner output), for private/offline use Whisper

#### 3. **Week 4 — Code Generation**
- Build on your Brochure Generator pattern: input → multi-step LLM pipeline → output
- **Tip:** Use the SAME multi-step approach you used in Week 1 Day 5 (link curator → assembler)

#### 4. **Week 5 — RAG (Retrieval Augmented Generation)**
- ChromaDB + LangChain are already installed
- **Tip:** Your knowledge-base could be a personal collection (e.g., Polish business/legal documents — building on your Day 1 SME analysis use case)
- Connect the RAG pipeline to a Gradio UI like you did in Week 2 Day 4–5

#### 5. **Week 6–7 — Fine-tuning**
- Wandb is in your stack — set up an account early (`wandb.init()` requires an API key)
- **Tip:** Track experiments early. Don't fine-tune blindly.
- The course uses HuggingFace `datasets==3.6.0` (pinned for compatibility)

#### 6. **Week 8 — Agentic AI**
- This builds on EVERYTHING. Tools (Week 2 Day 4) + RAG (Week 5) + Fine-tuning (Week 7) + Multi-step pipelines (Week 1 Day 5)
- **Tip:** Sketch the agent architecture on paper before coding. Identify which sub-agent does which task.

#### 7. **General Best Practices Going Forward**
- ✅ **Keep using SQLite** — you already proved it works better than dicts. Use it for any structured state.
- ✅ **Commit often with descriptive messages** — your commit history is already clean
- ✅ **Polish-language prompts work** — you've validated this in Week 1. Don't be afraid to keep using Polish for domain-specific tasks.
- ✅ **Save outputs as artifacts** — like you did with `image_Sydney.webp`. Helps when reviewing later.
- ⚠️ **Watch API costs** — Week 7 fine-tuning has optional ~$10 spend. Monitor `console.anthropic.com/settings/cost` and `platform.openai.com/usage`.
- ⚠️ **Pin model names in code** — you've used `gpt-4.1-mini`, `gpt-5-nano`, `claude-sonnet-4-5-20250929`. As models deprecate, update with intention.

#### 8. **Personal Recommendation**
- Consider creating a folder `lechuteq/projects/` for your own **portfolio projects** that build on the course (e.g., a Polish SME analyzer extending Week 1 Day 1, a multilingual chatbot extending Week 2 Day 3).
- Document each personal project in this folder with a small README — great for showcasing on LinkedIn or your GitHub profile later.

---

### 📦 Repository Structure (Your Work)

```
llm_engineering/
├── lechuteq/                        # ← Your personal documentation & artifacts
│   ├── LECHUTEQ_README.md           # ← This file
│   └── projects/                    # Portfolio standalone projects (Weeks 1-2)
├── week1/
│   ├── day1.ipynb                   # Customized: Polish SME analysis
│   ├── day2.ipynb                   # Customized: Ollama + Google API
│   ├── day4.ipynb                   # Modified
│   └── day5.ipynb                   # Brochure generator (refactored)
├── week2/
│   ├── day1.ipynb                   # Frontier model comparisons
│   ├── day2.ipynb                   # Gradio UIs
│   ├── day3.ipynb                   # Chatbot
│   ├── day4.ipynb                   # SQLite-backed Airline AI (custom!)
│   ├── day5.ipynb                   # Multimodal assistant
│   ├── image_Sydney.webp            # DALL-E 3 generated artifact
│   └── image_Warsaw.webp            # DALL-E 3 generated artifact
├── week3/
│   ├── Week 3 Day 1 - Colab.ipynb   # Colab setup + diffusers image gen
│   ├── Week 3 day 2 - pipelines.ipynb  # HF pipeline API (+ 2 custom prompts)
│   ├── Week 3 Day 3 - tokenizers.ipynb # Tokenizers deep-dive
│   ├── Week 3 Day 4 - models.ipynb  # AutoModelForCausalLM + 4-bit quant
│   └── Week 3 Day 5 - Meeting Minutes product.ipynb  # Audio → Whisper → Llama
└── CLAUDE.md                        # Claude Code guidance file
```

---

---

## 🇵🇱 WERSJA POLSKA

### Status synchronizacji (2026-06-19)

**Zgłaszany postęp:** 6 z 8 tygodni ukończonych.
**Zsynchronizowane z GitHub:** Tygodnie 1, 2, 3 (notebooki Colab z Tygodnia 3 wgrane 2026-06-19).
**Brakuje na tej maszynie:** prace z Tygodni 4, 5, 6.

Portfolio w [`projects/`](./projects/) odzwierciedla Tygodnie 1 i 2.

**Prawdopodobne lokalizacje brakującej pracy (do sprawdzenia w domu):**
- 🏠 Domowy komputer z Windows 11 — lokalny klon nigdy nie wypchnięty
- 🏠 Domowy komputer z Ubuntu — inny lokalny klon nigdy nie wypchnięty
- ☁️ Google Colab — sprawdź `colab.research.google.com → File → Recent notebooks`
- 📄 Luźne pliki `.ipynb` w folderach Pobrane / Dokumenty

**Polecenia wyszukiwania:**
```bash
# Linux / macOS / WSL
find / -name "day*.ipynb" -path "*week[4-8]*" 2>/dev/null

# Windows PowerShell
Get-ChildItem -Path C:\ -Recurse -Filter "day*.ipynb" -ErrorAction SilentlyContinue |
  Where-Object { $_.FullName -match "week[4-8]" }
```

**Następne kroki po znalezieniu:** Umieść je w `week4/`, `week5/` itd., zacommituj + wypchnij do origin, i rozszerz portfolio o projekty `05_`, `06_`, … odpowiednio.

---

### 📋 Przegląd postępów

| Tydzień | Dzień | Status | Temat |
|---------|-------|--------|-------|
| 1 | 1 | ✅ Gotowe (zsynchronizowane) | Podsumowywacz stron WWW (OpenAI) |
| 1 | 2 | ✅ Gotowe (zsynchronizowane) | Wielodostawcze API + Ollama |
| 1 | 4 | ✅ Gotowe (zsynchronizowane) | (zmodyfikowane) |
| 1 | 5 | ✅ Gotowe (zsynchronizowane) | Generator broszury firmowej |
| 2 | 1 | ✅ Gotowe (zsynchronizowane) | Porównanie modeli frontierowych |
| 2 | 2 | ✅ Gotowe (zsynchronizowane) | Interfejsy Gradio |
| 2 | 3 | ✅ Gotowe (zsynchronizowane) | Chatbot konwersacyjny |
| 2 | 4 | ✅ Gotowe (zsynchronizowane) | Asystent linii lotniczej z narzędziami (SQLite) |
| 2 | 5 | ✅ Gotowe (zsynchronizowane) | Multimodalny asystent AI |
| 3 | 1 | ✅ Gotowe (zsynchronizowane) | Colab + GPU + generowanie obrazów (diffusers) |
| 3 | 2 | ✅ Gotowe (zsynchronizowane) | Pipelines HuggingFace (wysokopoziomowe API) |
| 3 | 3 | ✅ Gotowe (zsynchronizowane) | Szczegółowa analiza tokenizatorów |
| 3 | 4 | ✅ Gotowe (zsynchronizowane) | Niskopoziomowe API modeli + kwantyzacja 4-bit |
| 3 | 5 | ✅ Gotowe (zsynchronizowane) | Produkt Protokołów ze spotkań (Audio → Whisper → Llama) |
| 4 | 1-5 | 🔍 Zrobione gdzie indziej — wymaga synchronizacji | Generowanie kodu |
| 5 | 1-5 | 🔍 Zrobione gdzie indziej — wymaga synchronizacji | RAG (Retrieval Augmented Generation) |
| 6 | 1-5 | 🔍 Zrobione gdzie indziej — wymaga synchronizacji | Fine-tuning |
| 7 | - | ⏳ W planach | Zaawansowany fine-tuning (Colab GPU) |
| 8 | - | ⏳ W planach | Agentic AI |

---

### 🗂️ TYDZIEŃ 1 — Podstawy korzystania z API LLM-ów

#### Dzień 1: Podsumowywacz stron WWW z OpenAI
**Cel:** Pierwsze zetknięcie z API Chat Completions OpenAI poprzez zbudowanie narzędzia, które pobiera zawartość strony WWW i zwraca jej podsumowanie w markdown.

**Co zostało zbudowane:**
- Web scraper z `BeautifulSoup` (przez plik pomocniczy `scraper.py`)
- Projektowanie promptów systemowych i użytkownika dla "uszczypliwych" streszczeń
- Wywołania OpenAI `gpt-4.1-mini` do podsumowywania
- Wyświetlanie markdown w Jupyterze przez `IPython.display`
- **Własne rozszerzenie pracy domowej:** Polski prompt do analizy biznesowej zaprojektowany do oceny MŚP (małych i średnich przedsiębiorstw) zgodnie z definicją UE, identyfikujący segment rynkowy, produkty vs. usługi, grupę docelową oraz porównujący je z konkurencją.

**Stack technologiczny:** Python, `openai`, `beautifulsoup4`, `requests`, `python-dotenv`, `IPython`, Jupyter Lab.

---

#### Dzień 2: Wielodostawcze modele Frontier + Ollama (lokalnie)
**Cel:** Eksploracja endpointów Chat Completions u różnych dostawców (OpenAI, Anthropic, Google, DeepSeek, Groq) i nauka, że dzielą one strukturę kompatybilną z OpenAI. Również uruchomienie lokalnego modelu przez Ollama.

**Co zostało zbudowane:**
- Równoległe wywołania wielu dostawców LLM przy użyciu zunifikowanego interfejsu klienta OpenAI
- Porównanie poziomów wysiłku rozumowania na `gpt-5-nano` i `gpt-5-mini`
- Test "trudnej zagadki" (zagadka z półką książek Puszkina)
- **Własna praca domowa:** Przebudowa podsumowywacza stron z Dnia 1 tak, by działał lokalnie z Ollama (`llama3.2`), udowadniając, że przepływ działa w pełni offline/darmowo.

**Stack technologiczny:** `openai`, `anthropic`, `google-generativeai`, `ollama`, `requests`.

---

#### Dzień 5: Generator broszury firmowej (analiza wielostronicowa)
**Cel:** Zbudowanie pełnego produktu biznesowego — mając tylko nazwę firmy + URL, automatycznie wykrywać istotne strony (O nas, Kariera, Produkty) i wygenerować broszurę sprzedażową.

**Co zostało zbudowane:**
- Dwuetapowy pipeline LLM:
  1. **Kurator linków** — wprowadza surowe linki strony do `gpt-5-nano` i prosi o istotne linki w ustrukturyzowanym JSON.
  2. **Składacz broszury** — łączy stronę główną + wybrane strony w jeden prompt i generuje broszurę w markdown.
- Strumieniowanie wyników dla doświadczenia "maszyny do pisania"
- Testy manualne z `huggingface.co` i `edwarddonner.com`

**Stack technologiczny:** `openai` (ustrukturyzowany JSON output), `beautifulsoup4`, strumieniowe odpowiedzi, Jupyter `update_display` dla renderowania na żywo.

**Uwaga:** Znaczący refactoring — oryginalny notatnik miał 1351 linii; finalny rozmiar to 403 linie (czysty i skonsolidowany).

---

### 🗂️ TYDZIEŃ 2 — Budowanie produktów AI dla użytkownika

#### Dzień 1: Porównanie modeli Frontier
**Cel:** Programowe porównanie modeli frontierowych na prostych pytaniach, zagadkach i zadaniach wymagających rozumowania.

**Co zostało zbudowane:**
- Zunifikowana konfiguracja klienta dla OpenAI, Anthropic, Google, DeepSeek, Groq
- Testy A/B promptów ("opowiedz dowcip dla studenta LLM Engineering", zagadki probabilistyczne, klasyczne rozumowanie)
- Testowanie różnych poziomów `reasoning_effort` (minimal / low / medium / high)
- 70 komórek eksperymentów porównujących wyniki modeli

**Stack technologiczny:** `openai`, `anthropic`, `google-generativeai`, `groq`, wzorce `litellm`.

---

#### Dzień 2: Interfejsy użytkownika w Gradio
**Cel:** Owinięcie funkcjonalności LLM w piękne, dające się udostępniać interfejsy webowe z użyciem Gradio.

**Co zostało zbudowane:**
- Proste callbacki `gr.Interface` (`fn=...`)
- Dodawanie autentykacji do aplikacji Gradio (`auth=(user, password)`)
- Wymuszanie trybu ciemnego
- UI strumieniowe oparte na generatorach z `yield`
- Wersja Gradio **generatora broszury firmowej** z Tygodnia 1 Dnia 5

**Stack technologiczny:** `gradio>=5.49`, generatory asynchroniczne, konfiguracja oparta o środowisko.

---

#### Dzień 3: AI konwersacyjne (Chatbot)
**Cel:** Zbudowanie stanowego asystenta czatu używając `gr.ChatInterface` ze świadomością historii.

**Co zostało zbudowane:**
- Wzorzec callbacka `chat(message, history)`
- Iteracyjne ulepszanie: bot przekazujący → bot echo → prawdziwe odpowiedzi LLM → z prompetem systemowym
- Persona "asystenta sklepu z ubraniami" z logiką promocyjną (czapki 60% taniej, inne przedmioty 50% taniej)
- Przykłady promptingu "one-shot" do zakotwiczenia zachowania modelu

**Stack technologiczny:** `gradio`, `openai`, inżynieria promptów systemowych.

---

#### Dzień 4: Asystent AI linii lotniczej z wywoływaniem narzędzi (SQLite!)
**Cel:** Wykorzystanie wywoływania narzędzi OpenAI (function calling), aby dać LLM dostęp do prawdziwego backendu.

**Co zostało zbudowane:**
- **Własne ulepszenie:** Migracja cen biletów ze słownika in-memory do **bazy SQLite** (`prices.db`) — znaczące ulepszenie w stosunku do domyślnej wersji kursu!
- Funkcja narzędziowa: `get_ticket_price(city)` z poprawną definicją JSON Schema
- Obsługa **wielu wywołań narzędzi w jednej odpowiedzi** (zaawansowany wzorzec)
- Sekwencyjna obsługa wywołań narzędzi (jedno po drugim)
- **Własna praca domowa:** Dodano narzędzie ustawiania cen (`set_ticket_price`) — spełnia specyfikację ćwiczenia z dnia

**Stack technologiczny:** wywoływanie narzędzi `openai`, `sqlite3`, `gradio.ChatInterface`, JSON Schema.

---

#### Dzień 5: Multimodalny asystent AI (Wizja + Audio)
**Cel:** Połączenie tekstu, generowania obrazów (DALL-E 3), audio (text-to-speech) i wywołań narzędzi w jednym agencie.

**Co zostało zbudowane:**
- Generator obrazów DALL-E 3 (`artist(city)`) — produkuje wakacyjne obrazy w stylu pop-art dla miast wykrytych przez narzędzie
- TTS audio z `gpt-4o-mini-tts` (głos: onyx)
- Niestandardowy layout UI `gr.Blocks` z Chatbotem + obrazem + audio obok siebie
- Przepływ narzędzi przechwytujący wspomniane miasta i dynamicznie generujący obrazy
- **Własne artefakty:** `image_Sydney.webp`, `image_Warsaw.webp` — wygenerowane obrazy zapisane jako dowód działania asystenta

**Stack technologiczny:** `openai` (chat + images + audio), `Pillow`, `base64`, `pydub`, `gradio.Blocks`.

---

### 🗂️ TYDZIEŃ 3 — Modele Open Source, HuggingFace i Google Colab

Wszystkie notebooki Tygodnia 3 uruchamiały się na **Google Colab** z darmowym GPU Tesla T4 (16 GB VRAM). Token `HF_TOKEN` był dostarczany przez Colab Secrets.

---

#### Dzień 1: Konfiguracja Google Colab + Generatywne modele obrazów
**Cel:** Pierwsze zetknięcie z Google Colab jako środowiskiem GPU w chmurze i uruchamianie najnowocześniejszych modeli dyfuzji obrazów bez lokalnego sprzętu.

**Co zostało zbudowane:**
- Sprawdzenie GPU przez `nvidia-smi` potwierdzające połączenie z Tesla T4
- Logowanie do HuggingFace z `HF_TOKEN` przez Colab Secrets
- Generowanie obrazów z **SDXL-Turbo** (`stabilityai/sdxl-turbo`) — szybka dyfuzja 4-krokowa
- Generowanie obrazów z **Stable Diffusion XL Base 1.0**
- **Pipeline dwóch modeli:** SDXL Base + SDXL Refiner łączone dla wyższej jakości
- Synteza mowy z `microsoft/speecht5_tts` + osadzenia głośnika z CMU Arctic
- Pokaz **FLUX.1-schnell** na premium GPU A100 (demo płatnego tierui z szacowaniem kosztów: ~$0.015/run)

**Stack technologiczny:** `diffusers`, `transformers`, `torch`, `datasets`, `soundfile`, `huggingface_hub`, GPU T4 Colab.

---

#### Dzień 2: Pipeline HuggingFace (Wysokopoziomowe API wnioskowania)
**Cel:** Opanowanie abstrakcji `pipeline()` z HuggingFace — jednego zunifikowanego API dla wielu zadań AI.

**Co zostało zbudowane / zbadane:**
- **Analiza sentymentu** — model domyślny + `nlptown/bert-base-multilingual-uncased-sentiment` (5 gwiazdek)
- **NER** — rozpoznawanie osób, organizacji, lokalizacji
- **Pytania i odpowiedzi** — ekstrakcyjne QA z kontekstem
- **Podsumowanie tekstu** — streszczenie abstrakcyjne
- **Tłumaczenie** — EN→FR (domyślne), EN→ES (`Helsinki-NLP/opus-mt-en-es`)
- **Klasyfikacja zero-shot** — tekst kategoryzowany w dowolne etykiety bez treningu
- **Generowanie tekstu** — otwarte generowanie w stylu GPT-2
- **Generowanie obrazów** — SDXL-Turbo przez `AutoPipelineForText2Image`
- **Audio (TTS)** — speecht5_tts przez pipeline

**Własne dodatki Lechuteq (komórki 20–21):**
- Osobisty prompt SDXL: *"Ciepło ubrany rowerzysta w czarnej kurtce narciarskiej jadący pomarańczowo-czarnym rowerem górskim w zaśnieżony, mroźny wieczór, kierujący się do swojego biura w białym domku — żywy styl pop-art"*
- Drugi osobisty prompt: *"Mały robot Python wyciągający dane z dokumentów PDF siedzący obok pracownika biurowego — ciemny styl pop-art"*

**Stack technologiczny:** `transformers.pipeline`, `diffusers`, `datasets`, `soundfile`, `torch`.

---

#### Dzień 3: Szczegółowa analiza tokenizatorów
**Cel:** Zrozumieć, co faktycznie dzieje się między słownikiem Python `messages=[]` a surowym tekstem wchodzącym do modelu — kluczowy "moment olśnienia" całego kursu.

**Co zostało zbadane:**
- `AutoTokenizer` załadowany dla **Meta Llama 3.1-8B**
- `tokenizer.encode()` / `decode()` / `batch_decode()` — kodowanie tekstu na ID tokenów i z powrotem
- Rozmiar słownika (`len(tokenizer.vocab)` = 128 000 dla Llama)
- **Warianty Instruct** — `Meta-Llama-3.1-8B-Instruct` używa szablonu czatu
- `tokenizer.apply_chat_template(messages)` — pokazuje rzeczywisty ciąg znaków, który widzi model
- **Porównanie tokenizatorów** między modelami: Llama 3.1, Phi-4 Mini, DeepSeek V3.1, QwenCoder 2.5
- Każdy model ma inny format szablonu czatu — kluczowy wgląd dla inżynierii promptów

**Stack technologiczny:** `transformers.AutoTokenizer`, HuggingFace Hub, CPU (bez GPU).

---

#### Dzień 4: Modele — Niskopoziomowe API Transformera
**Cel:** Zejść poniżej abstrakcji `pipeline()` i używać bezpośrednio `AutoModelForCausalLM` z tokenizacją, kwantyzacją i strumieniowaniem.

**Co zostało zbudowane:**
- **Kwantyzacja 4-bit** z `BitsAndBytesConfig` (`load_in_4bit=True`, `bnb_4bit_quant_type="nf4"`, podwójna kwantyzacja) — mieści duże modele w 16 GB T4
- Ładowanie **Llama 3.2-1B-Instruct** / **Llama 3.1-8B-Instruct** z `device_map="auto"` + konfiguracją kwant
- Raportowanie śladu pamięci: `model.get_memory_footprint()` — weryfikacja skompresowanego rozmiaru 4-bit
- Inspekcja surowego **obiektu modelu PyTorch** (warstwy, głowice uwagi, bloki MLP)
- `model.generate(inputs, max_new_tokens=80)` — surowe generowanie tokenów
- `TextStreamer` dla strumieniowania token po tokenie
- Wielokrotnie używalna funkcja pomocnicza `generate(model, messages, quant, max_new_tokens)`
- Testowane modele: **Phi** (Microsoft), **Gemma** (Google), **Qwen** (Alibaba), **DeepSeek**
- Czyszczenie pamięci: `del model, inputs; gc.collect(); torch.cuda.empty_cache()`

**Stack technologiczny:** `transformers` (`AutoModelForCausalLM`, `AutoTokenizer`, `TextStreamer`, `BitsAndBytesConfig`), `torch`, `bitsandbytes`, `accelerate`.

---

#### Dzień 5: Produkt Protokołów ze spotkań (Audio → Transkrypcja → Raport)
**Cel:** Zbudowanie realnego produktu end-to-end łączącego transkrypcję audio + generowanie tekstu LLM — generator protokołów ze spotkań.

**Co zostało zbudowane:**
- Montowanie Google Drive (`drive.mount("/content/drive")`) do dostępu do `denver_extract.mp3` (audio ze spotkania Rady Miejskiej Denver)
- **Krok 1 — Transkrypcja** (porównano dwie opcje):
  - Opcja A — Open source: `openai/whisper-medium.en` przez pipeline HuggingFace (automatyczne rozpoznawanie mowy ze znacznikami czasu)
  - Opcja B — Komercyjne: OpenAI API `gpt-4o-mini-transcribe`
  - Porównanie wyników obu transkrypcji obok siebie
- **Krok 2 — Generowanie protokołów:**
  - Prompt systemowy zaprojektowany do tworzenia ustrukturyzowanych protokołów: podsumowanie, kluczowe punkty, wnioski, zadania z właścicielami
  - Użyto `meta-llama/Llama-3.2-3B-Instruct` z kwantyzacją 4-bit + `TextStreamer`
  - Wynik renderowany w Markdown przez `IPython.display`

**Stack technologiczny:** `transformers` (Whisper ASR + Llama), `openai` (Whisper API), `BitsAndBytesConfig`, `google.colab.drive`, `IPython.display`.

---

### 🛠️ Wspólny Stack Technologiczny (Wszystkie tygodnie)

| Kategoria | Biblioteki |
|-----------|------------|
| SDK LLM | `openai`, `anthropic`, `google-generativeai`, `groq` |
| Lokalny LLM | `ollama` (llama3.2), HuggingFace `transformers` |
| Modele open source | Llama 3.1/3.2, Phi-4, Gemma, Qwen, DeepSeek, Whisper |
| Generowanie obrazów | `diffusers` (SDXL-Turbo, SDXL Base+Refiner, FLUX.1-schnell) |
| Mowa | `microsoft/speecht5_tts`, `openai/whisper-medium.en`, `gpt-4o-mini-tts` |
| Kwantyzacja | `bitsandbytes` (4-bit NF4), `accelerate` |
| UI | `gradio>=5.49` |
| Web scraping | `beautifulsoup4`, `requests` |
| Dane | `sqlite3` (własne usprawnienie!), `datasets==3.6.0` |
| Wyświetlanie | `IPython.display`, strumieniowanie Markdown |
| Media | `Pillow`, `base64`, `pydub`, `soundfile` |
| Chmura | Google Colab (darmowy T4 GPU, płatny A100) |
| Środowisko | `python-dotenv`, Colab Secrets (`userdata.get`) |
| Runtime | Python 3.12, Jupyter Lab 4.5, menedżer pakietów UV |

---

### 💡 Wskazówki na nadchodzące tygodnie (3–8)

Bazując na tym, co już zrobiłeś, oto jak sprawić by nadchodzące projekty błyszczały:

#### 1. **Wykorzystaj swoje wzorce**
Już opanowałeś:
- Strumieniowanie odpowiedzi → używaj `yield` w Gradio dla każdego długotrwałego zadania
- Wywoływanie narzędzi z SQLite → w Tygodniu 5 (RAG) możesz zamienić narzędzie SQLite na zapytanie do bazy wektorowej
- Layout `gr.Blocks` → używaj tego dla wszystkich złożonych UI w Tygodniach 4–8

#### 2. **Tydzień 3 — HuggingFace i modele Open Source (Colab) ✅ UKOŃCZONE**
- Zbudowałeś pełną progresję: pipelines → tokenizatory → surowe modele → realny produkt
- **Kluczowy wzorzec do ponownego użycia:** Funkcja pomocnicza `generate(model, messages, quant, max_new_tokens)` z Dnia 4 to standardowy sposób uruchamiania dowolnego kauzalnego modelu HuggingFace — skopiuj ją do fine-tuningu w Tygodniu 7
- **Kwantyzacja ma znaczenie:** 4-bit NF4 (`BitsAndBytesConfig`) pozwala modelom 8B parametrów zmieścić się w 16 GB T4 — zawsze używaj na darmowym tierze Colab
- **Whisper vs. komercyjne:** Porównałeś obie opcje transkrypcji — dla produkcji użyj gpt-4o-mini-transcribe (czystszy wynik), dla trybu prywatnego/offline użyj Whisper

#### 3. **Tydzień 4 — Generowanie kodu**
- Bazuj na wzorcu Generatora Broszury: input → wieloetapowy pipeline LLM → output
- **Wskazówka:** Użyj TAKIEGO SAMEGO podejścia wieloetapowego, jakie użyłeś w Tygodniu 1 Dniu 5 (kurator linków → składacz)

#### 4. **Tydzień 5 — RAG (Retrieval Augmented Generation)**
- ChromaDB + LangChain są już zainstalowane
- **Wskazówka:** Twoja baza wiedzy mogłaby być osobistą kolekcją (np. polskie dokumenty biznesowe/prawne — bazując na Twoim przypadku użycia analizy MŚP z Dnia 1)
- Połącz pipeline RAG z UI Gradio, tak jak w Tygodniu 2 Dniach 4–5

#### 5. **Tydzień 6–7 — Fine-tuning**
- Wandb jest w Twoim stacku — załóż konto wcześnie (`wandb.init()` wymaga API key)
- **Wskazówka:** Śledź eksperymenty od początku. Nie rób fine-tuningu w ciemno.
- Kurs używa HuggingFace `datasets==3.6.0` (przypięte dla kompatybilności)

#### 6. **Tydzień 8 — Agentic AI**
- Buduje się na WSZYSTKIM. Narzędzia (Tydzień 2 Dzień 4) + RAG (Tydzień 5) + Fine-tuning (Tydzień 7) + Pipeliny wieloetapowe (Tydzień 1 Dzień 5)
- **Wskazówka:** Naszkicuj architekturę agenta na papierze przed kodowaniem. Zidentyfikuj który sub-agent wykonuje które zadanie.

#### 7. **Ogólne najlepsze praktyki na przyszłość**
- ✅ **Używaj nadal SQLite** — już udowodniłeś, że działa lepiej niż słowniki. Używaj go dla każdego stanu strukturalnego.
- ✅ **Często commituj z opisowymi wiadomościami** — Twoja historia commitów jest już czysta
- ✅ **Polskie prompty działają** — zwalidowałeś to w Tygodniu 1. Nie bój się używać polskiego w zadaniach domenowych.
- ✅ **Zapisuj wyniki jako artefakty** — tak jak `image_Sydney.webp`. Pomaga przy późniejszym przeglądzie.
- ⚠️ **Uważaj na koszty API** — fine-tuning w Tygodniu 7 ma opcjonalny wydatek ~$10. Monitoruj `console.anthropic.com/settings/cost` i `platform.openai.com/usage`.
- ⚠️ **Przypinaj nazwy modeli w kodzie** — używałeś `gpt-4.1-mini`, `gpt-5-nano`, `claude-sonnet-4-5-20250929`. Gdy modele staną się przestarzałe, aktualizuj świadomie.

#### 8. **Osobista rekomendacja**
- Rozważ stworzenie folderu `lechuteq/projects/` na swoje własne **projekty portfolio** bazujące na kursie (np. analizator polskich MŚP rozszerzający Tydzień 1 Dzień 1, wielojęzyczny chatbot rozszerzający Tydzień 2 Dzień 3).
- Dokumentuj każdy osobisty projekt w tym folderze małym README — świetne do pokazania na LinkedIn lub Twoim profilu GitHub później.

---

### 📦 Struktura repozytorium (Twoja praca)

```
llm_engineering/
├── lechuteq/                        # ← Twoja osobista dokumentacja i artefakty
│   └── LECHUTEQ_README.md           # ← Ten plik
├── week1/
│   ├── day1.ipynb                   # Spersonalizowane: analiza polskich MŚP
│   ├── day2.ipynb                   # Spersonalizowane: Ollama + Google API
│   ├── day4.ipynb                   # Zmodyfikowane
│   └── day5.ipynb                   # Generator broszury (zrefactoryzowany)
├── week2/
│   ├── day1.ipynb                   # Porównania modeli frontierowych
│   ├── day2.ipynb                   # UI Gradio
│   ├── day3.ipynb                   # Chatbot
│   ├── day4.ipynb                   # Asystent linii lotniczej z SQLite (własne!)
│   ├── day5.ipynb                   # Multimodalny asystent
│   ├── add_example_cell.py          # Własny skrypt pomocniczy
│   ├── image_Sydney.webp            # Wygenerowany artefakt DALL-E 3
│   └── image_Warsaw.webp            # Wygenerowany artefakt DALL-E 3
└── CLAUDE.md                        # Plik wskazówek dla Claude Code
```

---

### 📚 Linki

- **Repozytorium autora:** https://github.com/ed-donner/llm_engineering
- **Twoje repozytorium:** https://github.com/Lechuteq/llm_engineering
- **Zasoby kursu:** https://edwarddonner.com/2024/11/13/llm-engineering-resources/
- **FAQ:** https://edwarddonner.com/faq/

---

*Dokument przygotowany: 27 maja 2026 | Zaktualizowany: 19 czerwca 2026 (Tydzień 3 dodany)*
*Document prepared: May 27, 2026 | Updated: June 19, 2026 (Week 3 added)*
