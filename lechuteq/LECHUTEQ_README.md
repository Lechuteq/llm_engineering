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
| 4 | 1-2 | 🔍 Missing — not on this machine | Code Generation (intro) |
| 4 | 3 | ✅ Done (synced) | Python → C++ with frontier models (4-way comparison) |
| 4 | 4 | ✅ Done (synced) | Gradio UI + 9-model benchmark |
| 4 | 5 | ✅ Done (synced) | Python → Rust extension + harder benchmark |
| 5 | 1 | ✅ Done (synced) | Keyword-based RAG — InsureLLM knowledge worker |
| 5 | 2 | ✅ Done (synced) | LangChain + ChromaDB vector store + t-SNE visualization |
| 5 | 3 | ✅ Done (synced) | LangChain RAG pipeline + Gradio chatbot |
| 5 | 4 | ✅ Done (synced) | RAG evaluation framework (accuracy/completeness/relevance) |
| 5 | 5 | ✅ Done (synced) | Advanced RAG: LLM chunking + reranking + query rewriting |
| 6 | 1 | ✅ Done (synced) | Data curation — 820k Amazon product scrape |
| 6 | 2 | ✅ Done (synced) | Data pre-processing — LLM summarization via Groq Batch API |
| 6 | 3 | ✅ Done (synced) | Baseline models — Linear Regression, Random Forest, XGBoost |
| 6 | 4 | ✅ Done (synced) | Neural network + frontier model benchmarking |
| 6 | 5 | ✅ Done (synced) | OpenAI fine-tuning (GPT-4.1-nano) |
| 7 | 1-5 | ✅ Done (synced) | QLoRA fine-tuning + model evaluation (Colab GPU) |
| 8 | 1 | ✅ Done (synced) | Modal.com cloud deployment + SpecialistAgent |
| 8 | 2 | ✅ Done (synced) | RAG vector store + FrontierAgent + EnsembleAgent |
| 8 | 3 | ✅ Done (synced) | ScannerAgent + MessagingAgent (Pushover) |
| 8 | 4 | ✅ Done (synced) | AutonomousPlanningAgent + agentic loop |
| 8 | 5 | ✅ Done (synced) | "The Price is Right" Gradio UI finale |

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

### 🗂️ WEEK 8 — Agentic AI: "The Price is Right"

The capstone project. A fully autonomous multi-agent system that scans the internet for product deals, estimates true product value using multiple AI strategies, and pushes notifications to your phone — all orchestrated by a planning agent inside a Gradio UI.

**Agent architecture:**

```
DealAgentFramework
├── ScannerAgent       — scrapes deal sites, uses GPT to select top 5
├── EnsembleAgent
│   ├── FrontierAgent      — RAG over 400k Amazon products + GPT-5.1
│   ├── SpecialistAgent    — fine-tuned Llama on Modal.com cloud
│   └── NeuralNetworkAgent — deep neural network from Week 6
├── MessagingAgent     — Pushover push notifications to phone
└── AutonomousPlanningAgent — LLM-driven tool-calling orchestration loop
```

---

#### Day 1: Modal.com Cloud Deployment + SpecialistAgent
**Goal:** Deploy a fine-tuned LLM as a production-grade API service on Modal.com (serverless GPU cloud), then wire it into the first agent.

**What was built:**
- Modal.com account setup + API token configuration (`modal token set`)
- `hello.py` — simple Modal app demonstrating local vs. remote execution and EU region routing
- `llama.py` — Llama text generation deployed as a Modal remote function (`generate.remote()`)
- `pricer_ephemeral.py` — ephemeral Modal app: sends product description → returns price estimate using the Week 6 fine-tuned model
- `pricer_service.py` / `pricer_service2.py` — persistent **deployed** Modal services (survived beyond notebook session)
- `Preprocessor` class — cleans product descriptions before sending to the pricer (uses Llama 3.2 or Groq)
- `SpecialistAgent` — wraps the deployed Modal pricer behind a clean `.price(description)` interface
- Explored keeping Modal containers warm to eliminate 30-second cold-start latency

**Tech stack:** `modal`, `agents/specialist_agent.py`, `agents/preprocessor.py`, `litellm`.

---

#### Day 2: RAG Vector Store + FrontierAgent + EnsembleAgent
**Goal:** Build a RAG-powered pricing agent over 400,000 scraped Amazon products, then combine all pricing strategies into an ensemble.

**What was built:**
- ChromaDB persistent vector store (`products_vectorstore/`) populated with embeddings of 400k Amazon product descriptions
- `sentence-transformers/all-MiniLM-L6-v2` for encoding (384-dimensional vectors)
- t-SNE dimensionality reduction + Plotly 2D/3D interactive scatter plot to visualize product clusters by category
- `find_similars(item)` — semantic search: given a product, find 5 similar products and their prices
- `make_context()` — builds a RAG context block of similar products to inject into the LLM prompt
- `gpt_5_1_rag(item)` — `gpt-5.1` with RAG context + `reasoning_effort="none"` + `seed=42`
- **EnsembleAgent** — weighted average: RAG frontier (80%) + Modal specialist (10%) + neural network (10%)
- `FrontierAgent` class — encapsulates the RAG + GPT-5.1 pipeline
- `NeuralNetworkAgent` class — wraps the deep neural network from Week 6
- `EnsembleAgent` class — combines all three strategies

**Tech stack:** `chromadb`, `sentence-transformers`, `sklearn` (t-SNE), `plotly`, `litellm`, `modal`, `agents/frontier_agent.py`, `agents/neural_network_agent.py`, `agents/ensemble_agent.py`.

---

#### Day 3: ScannerAgent + MessagingAgent (Pushover)
**Goal:** Build agents that find deals on the internet and send push notifications to a phone.

**What was built:**
- `ScrapedDeal.fetch()` — scrapes deal aggregator sites for product listings
- GPT-5-mini with structured JSON output (`response_format=DealSelection`) to select the 5 most promising deals with clear prices
- `ScannerAgent` — wraps fetch + LLM filtering into a clean `.scan()` interface
- **Pushover integration** — push notifications to phone via `https://api.pushover.net/1/messages.json`
- `MessagingAgent` — wraps Pushover with `.push(message)` and `.notify(description, deal_price, true_value, url)` methods
- End-to-end test: `agent.notify("Samsung 60 inch LED TV", 300, 1000, "www.samsung.com")` → phone notification

**Tech stack:** `openai` (structured output, `reasoning_effort="minimal"`), `requests` (Pushover API), `agents/scanner_agent.py`, `agents/messaging_agent.py`, `agents/deals.py`.

---

#### Day 4: AutonomousPlanningAgent (Agentic Loop)
**Goal:** Build a fully autonomous agent that plans its own multi-step workflow using LLM-driven tool calling — no hardcoded sequence.

**What was built:**
- Prototype with 3 fake stub functions to understand the agent loop pattern:
  - `scan_the_internet_for_bargains()` → returns hardcoded deals
  - `estimate_true_value(description)` → always returns $300
  - `notify_user_of_deal(description, deal_price, estimate, url)` → prints message
- JSON Schema tool definitions for all three functions
- **Agent loop:** `while not done: response = openai.chat.completions.create(..., tools=tools)` — LLM decides which tools to call and in what order
- `handle_tool_call(message)` — dispatches tool calls dynamically via `globals().get(tool_name)`
- **AutonomousPlanningAgent** — swaps fake stubs for real agents (ScannerAgent → EnsembleAgent → MessagingAgent), fully autonomous end-to-end pipeline
- `agent.plan()` — triggers the full autonomous deal-hunting loop

**Tech stack:** `openai` (tool calling, `gpt-5.1`), `chromadb`, `agents/autonomous_planning_agent.py`, `agents/scanner_agent.py`, `agents/ensemble_agent.py`.

---

#### Day 5: "The Price is Right" — Gradio UI Finale
**Goal:** Wrap the entire multi-agent system in a polished Gradio UI and ship the capstone product.

**What was built:**
- Iterative Gradio `gr.Blocks` UI construction (built piece by piece in notebook)
- Final UI layout: deal list table + opportunity display + live agent log
- `DealAgentFramework` — orchestrates all agents, manages `memory.json` (persists discovered deals across runs)
- `DealAgentFramework.reset_memory()` — resets deal history
- `price_is_right.py` — standalone launchable product (`uv run price_is_right.py`)
- The product continuously scans, prices, and notifies — fully autonomous, runs indefinitely

**Tech stack:** `gradio` (`gr.Blocks`, `gr.DataFrame`, `gr.Timer`), `deal_agent_framework.py`, `agents/` package, `memory.json`.

---

### 🗂️ WEEK 4 — Code Generation: Python → C++ / Rust

Use frontier LLMs to translate Python code into high-performance compiled languages (C++ and Rust), benchmark the results, and wrap everything in a Gradio UI.

> **Note:** Days 1 & 2 notebooks are not on this machine — missing from sync. Days 3–5 are present.

---

#### Day 3: Python → C++ Code Generator (4-Model Comparison)
**Goal:** Build a code conversion tool that translates Python into optimized C++ and actually benchmark the speedup on a real computation.

**What was built:**
- `system_info.py` — detects machine OS, CPU, and available C++ compiler, then asks GPT to provide the right compile command for the host system
- Compile pipeline: `clang++` with maximum optimizations (`-Ofast -mcpu=native -flto=thin -DNDEBUG`) → native binary
- System prompt: *"convert Python to high-performance C++, respond only with code"*
- `port(client, model, python)` → strips markdown fences, writes `main.cpp`, compiles and runs
- Benchmark: π calculation with 200,000,000 iterations — Python baseline **~19.18 seconds**

**4-model benchmark results:**

| Place | Model | Time (s) | Speedup |
|-------|-------|----------|---------|
| 4th | Claude Sonnet 4.5 | 0.104 | ~184× |
| 3rd | GPT-5 | 0.082 | ~233× |
| 2nd | Grok 4 | 0.018 | ~1,060× |
| 1st | Gemini 2.5 Pro | 0.013 | **~1,440×** |

**Tech stack:** `openai`, `anthropic`, `subprocess` (compile + run), `system_info.py`.

---

#### Day 4: Gradio UI + 9-Model Expanded Benchmark
**Goal:** Add a Gradio UI for interactive Python→C++ conversion with any model, and expand the competition to 9 models including open-source alternatives.

**What was built:**
- `gr.Blocks` UI: Python code editor (left) → C++ output (right), model dropdown selector, Convert button
- Extended model roster with 9 models across 6 providers:
  - Frontier: GPT-5, Claude Sonnet 4.5, Grok 4, Gemini 2.5 Pro
  - Open source via Groq/OpenRouter: `openai/gpt-oss-120b`, `gpt-oss:20b`
  - Code-specialized: Qwen 2.5 Coder (Ollama), DeepSeek Coder v2 (Ollama), Qwen3 Coder 30B (OpenRouter)
- `port(model, python)` refactored to use `clients[model]` dispatch dict
- `reasoning_effort="high"` applied selectively for GPT models

**9-model benchmark results (same π benchmark):**

| Place | Model | Speedup |
|-------|-------|---------|
| 9th | Qwen 2.5 Coder | FAIL |
| 8th | OpenAI gpt-oss-120B | 14× |
| 7th | DeepSeek Coder v2 | 168× |
| 6th | Qwen3 Coder 30B | 168× |
| 5th | Claude Sonnet 4.5 | 184× |
| 4th | GPT-5 | 233× |
| 3rd | gpt-oss-20B | 238× |
| 2nd | Grok 4 | 1,060× |
| 1st | Gemini 2.5 Pro | **1,440×** |

**Tech stack:** `gradio` (`gr.Blocks`, `gr.Dropdown`, `gr.Textbox`), all 6 provider clients.

---

#### Day 5: Rust Extension + Harder Benchmark + Styled UI
**Goal:** Extend the code generator to target Rust (not just C++), add a harder algorithmic benchmark, and polish the Gradio UI.

**What was built:**
- `language = "Rust"` / `"C++"` toggle — system prompt and file extension adapt automatically
- Rust compile pipeline: `rustc -C opt-level=3 -C target-cpu=native -C lto=fat -C panic=abort -C strip=symbols`
- **Harder benchmark:** max subarray sum with LCG (Linear Congruential Generator) random numbers — requires 64-bit integer arithmetic support (many models failed this)
- `styles.py` CSS + `gr.themes.Monochrome()` + `gr.Code` with syntax highlighting (Python/C++/Rust)
- `compile_and_run(code)` now returns output string (piped back into Gradio)

**Harder benchmark results (most models failed):**

| Place | Model | Time (s) | Speedup vs Python |
|-------|-------|----------|-------------------|
| FAIL | Qwen 2.5 Coder, Gemini 2.5 Pro, DeepSeek Coder v2, Qwen3 30B, Claude Sonnet 4.5, GPT-5 | — | — |
| 3rd | gpt-oss-20B | 0.000341 | ~99,000× |
| 2nd | Grok 4 | 0.000317 | ~106,000× |
| 1st | OpenAI gpt-oss-120B | 0.000304 | **~110,000×** |

**Tech stack:** `gradio` (`gr.Code`, `gr.themes.Monochrome`), `styles.py`, `rustc`, `subprocess`.

---

### 🗂️ WEEK 5 — RAG: Expert Knowledge Worker for InsureLLM

Build a question-answering assistant for a fictional insurance tech company (InsureLLM) using a knowledge base of employee profiles, product sheets, and contracts — progressing from naive keyword matching to advanced RAG with reranking and query rewriting.

---

#### Day 1: Keyword-Based RAG (Baseline)
**Goal:** Build the simplest possible RAG — no vectors, just keyword lookup — to establish a working chatbot before introducing complexity.

**What was built:**
- Loaded all knowledge-base `.md` files (employees, products, contracts) into a Python dict keyed by last name / product name
- `get_relevant_context(message)` — splits user message into words, looks each up in the dict → returns matching documents
- `additional_context(message)` — wraps context into a formatted string injected into the system prompt
- Full `chat(message, history)` function using `gpt-4.1-nano` (cost-optimized choice)
- Launched as `gr.ChatInterface` — working chatbot in one screen of code

**Tech stack:** `openai` (`gpt-4.1-nano`), `glob`, `pathlib`, `gradio`.

---

#### Day 2: LangChain + ChromaDB Vector Store + t-SNE Visualization
**Goal:** Replace keyword lookup with semantic vector search — chunk documents, embed them, store in ChromaDB, and visualize the embedding space.

**What was built:**
- `tiktoken` token count analysis of the full knowledge base
- LangChain `DirectoryLoader` + `TextLoader` to load all `.md` files with `doc_type` metadata
- `RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)` — divided documents into chunks
- Two embedding options compared:
  - `HuggingFaceEmbeddings("all-MiniLM-L6-v2")` — free, local, 384 dimensions
  - `OpenAIEmbeddings("text-embedding-3-large")` — paid, higher quality
- `Chroma.from_documents()` — populated persistent vector store (`vector_db/`)
- t-SNE 2D and 3D scatter plots (Plotly) — visualized how document types cluster in embedding space

**Tech stack:** `langchain-openai`, `langchain-chroma`, `langchain-huggingface`, `langchain-community`, `tiktoken`, `chromadb`, `sklearn` (t-SNE), `plotly`, `numpy`.

---

#### Day 3: LangChain RAG Pipeline + Gradio Chatbot
**Goal:** Wire the vector store into a full LangChain RAG pipeline with a one-function Gradio chatbot.

**What was built:**
- `vectorstore.as_retriever()` — LangChain retriever over the ChromaDB store
- `ChatOpenAI(temperature=0, model_name="gpt-4.1-nano")` — deterministic answers
- `retriever.invoke(question)` + `llm.invoke(...)` — demonstrated both objects independently
- `answer_question(question, history)` — retrieves docs, formats context, calls LLM via `SystemMessage` + `HumanMessage`
- `gr.ChatInterface(answer_question).launch()` — full chatbot in 3 lines

**Tech stack:** `langchain-openai` (`ChatOpenAI`), `langchain-chroma`, `langchain-core`, `gradio`.

---

#### Day 4: RAG Evaluation Framework
**Goal:** Measure RAG quality systematically — not just "does it answer", but accuracy, completeness, and relevance scored by an LLM judge.

**What was built:**
- `evaluation/tests.jsonl` — test suite with questions, reference answers, categories, and expected keywords
- `evaluate_retrieval(example)` — checks whether the retrieved chunks actually contain relevant content
- `evaluate_answer(example)` — calls an LLM judge that scores the answer on:
  - `accuracy` — factual correctness
  - `completeness` — covers all required points
  - `relevance` — stays on topic
- `eval.feedback` — natural language explanation of the score
- Category breakdown via `Counter` — identifies which question types the RAG struggles with

**Tech stack:** `evaluation/` package, `langchain`, custom Pydantic evaluation models.

---

#### Day 5: Advanced RAG — LLM Chunking + Reranking + Query Rewriting
**Goal:** Replace every LangChain abstraction with a custom implementation and add three advanced techniques to significantly improve retrieval quality.

**What was built:**
- **LLM-driven chunking** (no LangChain): LLM reads each document and produces structured `Chunk` objects (`headline`, `summary`, `content`) using Pydantic + `response_format` — semantically meaningful chunks instead of fixed character splits
- **OpenAI embeddings** (`text-embedding-3-large`) stored in ChromaDB (`pro_implementation/`)
- **Reranking:** retrieved top-K chunks are re-ordered by a second LLM call that scores relevance — surfaces buried results (`RankOrder` Pydantic model)
- **Query rewriting:** user's question is rewritten by an LLM to be more specific and more likely to surface relevant content before hitting the vector store
- t-SNE visualization of the pro chunk embeddings (richer clusters than Day 2)
- Final `answer_question(question, history)` pipeline: rewrite → fetch → rerank → generate

**Tech stack:** `openai` (embeddings + chat), `chromadb` (native, no LangChain), `pydantic`, `litellm`, `sklearn` (t-SNE), `plotly`, `tqdm`.

---

### 🗂️ WEEK 6 — "The Price is Right": Data Preparation + Classical ML + Neural Networks

Build a product price predictor from scratch using 820,000 scraped Amazon product descriptions. This week establishes all the training data and baseline models that Weeks 7 and 8 build on.

---

#### Day 1: Data Curation — 820k Amazon Product Scrape
**Goal:** Acquire, clean, and curate a large real-world dataset from multiple Amazon product categories — learning data engineering at scale.

**What was built:**
- Loaded 8 Amazon product categories from `McAuley-Lab/Amazon-Reviews-2023` HuggingFace dataset
- `Item` class — parses each product into title, price, category, weight, and description text
- Price filter: $1–$1,000 range; description length/quality filter to remove poor entries
- Distribution analysis (matplotlib): price histograms, character length histograms, price vs. weight scatter plots
- **Stratified sampling**: 820,000-item final dataset sampled with price-weighted probability (squares prices to avoid over-weighting cheap items), with Tools/Automotive categories down-sampled
- Deduplication by title and full text
- 80/10/10 train/val/test split — pushed to `ed-donner/items_raw_lite` and `items_raw_full` on HuggingFace Hub

**Tech stack:** `datasets` (HuggingFace), `pricer/items.py`, `pricer/loaders.py`, `matplotlib`, `numpy`, `tqdm`.

---

#### Day 2: Data Pre-processing — LLM Summarization via Groq Batch API
**Goal:** Clean and rewrite 820k raw Amazon product descriptions into concise, structured summaries using LLM batch processing (at < $1 for Lite, ~$30 for Full).

**What was built:**
- System prompt designed to rewrite product descriptions into a fixed 5-field format: Title, Category, Brand, Description (1 sentence), Details (1 sentence)
- Tested two models for summarization: `groq/openai/gpt-oss-20b` and local `ollama/llama3.2`
- **Groq Batch API**: built JSONL files (1,000 items/file), uploaded via `groq.files.create()`, submitted via `groq.batches.create()`, polled and downloaded results
- `Batch` class — wraps the entire create/run/fetch lifecycle with progress tracking
- Final summarized dataset pushed to HuggingFace Hub as `items_lite` / `items_full`

**Tech stack:** `litellm`, `groq` (Batch API), `pricer/batch.py`, `json`, HuggingFace Hub.

---

#### Day 3: Baselines + Traditional ML Models
**Goal:** Establish evaluation metrics and build a progression of classical ML models as price predictors.

**What was built:**
- `evaluate(pricer_fn, test)` — RMSE-based evaluation function (lower = better)
- Baseline models:
  - `random_pricer` — random $1–$1,000 (sanity check)
  - `constant_pricer` — always predicts training mean (~$106)
  - **Linear Regression** on 3 numeric features: weight, weight_unknown flag, text_length — RMSE 101.56
  - **NLP + Linear Regression**: `CountVectorizer(max_features=2000)` bag-of-words → RMSE 76.81
  - **Random Forest** (100 trees, n_jobs=4) on same BoW features — RMSE 72.28
  - **XGBoost** (1000 trees, gradient boosting) — RMSE 68.23

**Tech stack:** `scikit-learn` (LR, RF, `CountVectorizer`), `xgboost`, `pandas`, `numpy`.

---

#### Day 4: Neural Network from Scratch + Frontier Model Benchmarking
**Goal:** Build a custom PyTorch neural network and pit it against frontier LLMs — zero-shot, no training.

**What was built:**
- **Human benchmark**: exported 100 test items to CSV, had a human price them — RMSE 87.62 (worse than XGBoost!)
- **8-layer PyTorch Neural Network** (`HashingVectorizer` 5,000 BoW features → 128 → 64 → 32 → 16 → 8 → 4 → 1):
  - Adam optimizer, MSE loss, 2 epochs — RMSE 63.97
- **Frontier model benchmarking** (zero-shot pricing, no training):
  - `gpt-4.1-nano`: RMSE 62.51
  - `claude-opus-4-5`: evaluated
  - `gemini-3-pro-preview`: RMSE 50.54
  - `gemini-2.5-flash-lite`: evaluated
  - `grok-4-1-fast`: RMSE 57.62
  - `gpt-5.1` (`reasoning_effort="high"`): RMSE **44.74** (best so far)
- All frontier model calls via `litellm.completion()` with parallel workers

**Tech stack:** `torch`, `torch.nn`, `torch.optim`, `sklearn` (`HashingVectorizer`, `train_test_split`), `litellm`, `csv`.

---

#### Day 5: OpenAI Fine-tuning (GPT-4.1-nano)
**Goal:** Fine-tune `gpt-4.1-nano` on the Amazon pricing dataset and measure improvement over the base model.

**What was built:**
- JSONL prompt format: `user` → product summary, `assistant` → `$price` — uploaded to OpenAI Files API
- `openai.fine_tuning.jobs.create()` with `gpt-4.1-nano-2025-04-14`, `n_epochs=1`, `suffix="pricer"`
- Polled job status via `openai.fine_tuning.jobs.retrieve()` and `list_events()`
- Tested fine-tuned model with `max_tokens=7` (only needs to output a number)
- **Results by training size**:
  - 100 examples → RMSE 96.58 (barely better than base)
  - 200 examples → RMSE 79.29
  - 2,000 examples → RMSE 82.26
  - **20,000 examples → RMSE 67.75** (matches Random Forest territory)

**Bonus — Deep Neural Network (Optional Extra):**
- `pricer/deep_neural_network.py` — larger, more expressive network trained for 5 epochs on the full 800k dataset (~4 hours on M1 Mac GPU)
- Pre-trained weights downloadable from Google Drive (`deep_neural_network.pth`)
- RMSE **46.49** — competitive with frontier models, used in Week 8 EnsembleAgent

**Tech stack:** `openai` (Files API, Fine-tuning API), `torch` (deep neural network), HuggingFace Hub.

---

### 🗂️ WEEK 7 — Fine-tuning with QLoRA: "The Price is Right"

Fine-tune **Llama 3.2-3B** on 400,000 Amazon product descriptions to predict product prices from text — and beat every frontier model including GPT-5.1.

All training ran on Google Colab (T4 for Lite mode, A100 for Full mode). The repo contains both the original day notebooks (with Colab links) and updated `NEW_` versions with full code.

---

#### Day 1: Introduction to LoRA & QLoRA
**Goal:** Understand the theory and math behind LoRA (Low-Rank Adaptation) before training — why it works, how much memory it saves, and how to read the adapter weights.

**What was explored:**
- Loading Llama 3.2-3B in three precisions and comparing memory footprint:
  - Full precision: ~6.4 GB
  - 8-bit: ~3.2 GB
  - 4-bit NF4 (double quant): ~1.9 GB
- Loading a fine-tuned model on top of the 4-bit base with `PeftModel.from_pretrained()`
- **LoRA math:** each target module gets two low-rank adapter matrices `lora_A` and `lora_B`, and weights are updated as `base + alpha * lora_A @ lora_B`
- Calculated trainable parameter counts:
  - **Lite mode** (`r=32`, attention layers only): ~13M trainable params out of 3B total
  - **Full mode** (`r=256`, attention + MLP layers): significantly more, covering the whole model

**Tech stack:** `transformers`, `peft` (`LoraConfig`, `PeftModel`), `bitsandbytes`, Colab T4.

---

#### Day 2: Prompt Data Preparation + Base Model Evaluation
**Goal:** Shape the raw Amazon dataset into fine-tuning prompts, then measure the base model's performance as a baseline.

**What was built:**
- Loaded `ed-donner/items_prompts_lite` (Lite) or `ed-donner/items_prompts_full` (Full) from HuggingFace Hub
- Token count histogram — cutoff set at 110 tokens (truncates ~X% of items)
- `item.make_prompts(tokenizer, cutoff, include_price)` — builds training prompt + completion pairs
- Prompt format: product description → model must generate just the price as a number
- Pushed prompt datasets back to HuggingFace Hub
- **Base model evaluation:** `model_predict(item)` with `max_new_tokens=8` on Llama 3.2-3B 4-bit
- Baseline RMSE: **110.72** — worse than a constant predictor (the base model has no pricing knowledge)

**Tech stack:** `transformers` (`AutoTokenizer`), `datasets`, `huggingface_hub`, `matplotlib`.

---

#### Days 3 & 4: QLoRA Training
**Goal:** Fine-tune Llama 3.2-3B with QLoRA using Supervised Fine-Tuning Trainer (`SFTTrainer`) and track with Weights & Biases.

**What was built:**
- **Quantization config:** 4-bit NF4, double quant, bfloat16 compute dtype
- **LoRA config** (`LoraConfig`): `r`, `lora_alpha`, `lora_dropout`, `task_type="CAUSAL_LM"`, `target_modules`
- **Training config** (`SFTConfig`):
  - Lite mode: 1 epoch, batch size 32, T4 GPU
  - Full mode: 3 epochs, batch size 256, A100 GPU
  - Optimizer, gradient accumulation, warmup ratio, cosine LR scheduler, weight decay 0.001
- **W&B integration:** `wandb.init(project=PROJECT_NAME)` — logged loss curves and eval metrics
- `SFTTrainer.train()` — ran fine-tuning, checkpointed every `SAVE_STEPS`
- `fine_tuning.model.push_to_hub(PROJECT_RUN_NAME, private=True)` → pushed to `UserPWG/price-{timestamp}` on HuggingFace

**Tech stack:** `transformers` (`TrainingArguments`), `trl` (`SFTTrainer`, `SFTConfig`), `peft` (`LoraConfig`), `bitsandbytes`, `wandb`, Colab T4 (Lite) / A100 (Full).

---

#### Day 5: Evaluation & Results
**Goal:** Measure the fine-tuned model against all baselines and frontier models.

**Benchmark results (RMSE — lower is better):**

| Model | RMSE | Type |
|-------|------|------|
| Constant baseline | 106.18 | Baseline |
| Base Llama 3.2 4-bit | 110.72 | Open source (untrained) |
| Linear Regression | 101.56 | Classical ML |
| Random Forest | 72.28 | Classical ML |
| XGBoost | 68.23 | Classical ML |
| Human (Ed) | 87.62 | Human |
| GPT-4.1 Nano | 62.51 | Frontier |
| Neural Network | 63.97 | Custom DNN |
| Fine-tuned Lite | 65.40 | Fine-tuned (T4, 1 epoch) |
| Grok 4.1 Fast | 57.62 | Frontier |
| Gemini 3 Pro | 50.54 | Frontier |
| Claude 4.5 Sonnet | 47.10 | Frontier |
| Deep Neural Network | 46.49 | Custom DNN (Week 6) |
| GPT-5.1 | 44.74 | Frontier (best commercial) |
| **Fine-tuned Full** | **39.85** | **Fine-tuned (A100, 3 epochs) 🏆** |

**Key insight:** The Fine-tuned Full model (39.85 RMSE) **beats every frontier model** including GPT-5.1 — despite being a 3B parameter model vs. GPT-5.1's trillions. Domain-specific fine-tuning on 400k examples wins over raw model size.

**Tech stack:** `plotly` (benchmark bar chart), `transformers`, `peft`.

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
| Cloud | Google Colab (T4/A100 GPU), Modal.com (serverless GPU) |
| Agentic AI | `modal`, `chromadb`, `sentence-transformers`, Pushover API, `agents/` package |
| Env | `python-dotenv`, Colab Secrets, Modal Secrets |
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

#### 3. **Week 4 — Code Generation ✅ DONE (Days 3–5)**
- Gemini 2.5 Pro won the C++ benchmark (1,440× speedup); gpt-oss-120B won the harder Rust benchmark (110,000×)
- **Key insight:** `reasoning_effort="high"` matters for code generation — apply it selectively to GPT models
- **The provider dispatch dict pattern** (`clients[model]`) is clean and reusable — generalizes to any multi-provider comparison
- Days 1–2 still missing from this machine — find on Win11/Ubuntu

#### 4. **Week 5 — RAG ✅ DONE**
- The progression Day 1→5 is the cleanest learning arc in the course: keyword dict → LangChain → raw ChromaDB + reranking + query rewriting
- **Key reusable pattern:** Day 5's `rewrite → fetch → rerank → generate` pipeline is production-grade RAG — use it in any future knowledge-base project
- **LLM chunking beats fixed-size chunking:** semantic chunks (Day 5) produce much richer t-SNE clusters than character splits (Day 2)

#### 5. **Week 6–7 — Fine-tuning ✅ DONE**
- Your fine-tuned full model (39.85 RMSE) beat GPT-5.1 (44.74) — the headline result of the whole course
- **Key takeaway:** Domain-specific fine-tuning on enough data beats raw model size. A 3B model with 400k examples outperforms a trillion-parameter frontier model
- **W&B tracking proved its worth:** experiment logs let you compare Lite vs. Full training runs without re-running everything
- **QLoRA pattern is reusable:** the `LoraConfig` + `SFTTrainer` + `push_to_hub` pipeline from Days 3-4 is the standard recipe for any future fine-tuning task

#### 6. **Week 8 — Agentic AI ✅ DONE**
- You built the full capstone: ScannerAgent → EnsembleAgent (RAG + Modal specialist + neural net) → MessagingAgent → AutonomousPlanningAgent → Gradio UI
- **Key pattern:** The agentic `while not done` loop with `handle_tool_call()` is reusable for any autonomous agent — it's the same pattern as Week 2 Day 4, massively scaled up
- **Modal.com is production deployment:** `modal deploy` converts your local code into a scalable cloud API — use this pattern for any ML model you want to serve at scale
- **EnsembleAgent insight:** 80/10/10 weighting (frontier RAG / specialist / neural net) outperformed any single model alone — ensemble thinking is a core ML engineering skill

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
├── week4/                           # Days 3-5 synced; Days 1-2 missing
├── week5/                           # RAG + LangChain + ChromaDB — fully synced
├── week6/                           # Fine-tuning data prep — fully synced
├── week7/                           # QLoRA fine-tuning — fully synced
└── week8/
    ├── agents/                      # Full multi-agent package
    ├── day1.ipynb                   # Modal.com + SpecialistAgent
    ├── day2.ipynb                   # RAG + FrontierAgent + EnsembleAgent
    ├── day3.ipynb                   # ScannerAgent + MessagingAgent
    ├── day4.ipynb                   # AutonomousPlanningAgent
    ├── day5.ipynb                   # Gradio UI finale
    ├── deal_agent_framework.py      # Orchestrator + memory.json
    └── price_is_right.py            # Standalone launchable product
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
| 4 | 1-2 | 🔍 Brak — nie na tej maszynie | Generowanie kodu (wprowadzenie) |
| 4 | 3 | ✅ Gotowe (zsynchronizowane) | Python → C++ z modelami frontier (porównanie 4 modeli) |
| 4 | 4 | ✅ Gotowe (zsynchronizowane) | UI Gradio + benchmark 9 modeli |
| 4 | 5 | ✅ Gotowe (zsynchronizowane) | Rozszerzenie Python → Rust + trudniejszy benchmark |
| 5 | 1 | ✅ Gotowe (zsynchronizowane) | RAG słownikowy — pracownik wiedzy InsureLLM |
| 5 | 2 | ✅ Gotowe (zsynchronizowane) | LangChain + ChromaDB + wizualizacja t-SNE |
| 5 | 3 | ✅ Gotowe (zsynchronizowane) | Pipeline RAG LangChain + chatbot Gradio |
| 5 | 4 | ✅ Gotowe (zsynchronizowane) | Framework ewaluacji RAG |
| 5 | 5 | ✅ Gotowe (zsynchronizowane) | Zaawansowany RAG: chunking LLM + reranking + przepisywanie zapytań |
| 6 | 1 | ✅ Gotowe (zsynchronizowane) | Kuracja danych — 820k produktów Amazon |
| 6 | 2 | ✅ Gotowe (zsynchronizowane) | Pre-processing — podsumowania LLM przez Groq Batch API |
| 6 | 3 | ✅ Gotowe (zsynchronizowane) | Modele bazowe — regresja liniowa, Random Forest, XGBoost |
| 6 | 4 | ✅ Gotowe (zsynchronizowane) | Sieć neuronowa + benchmarking modeli frontier |
| 6 | 5 | ✅ Gotowe (zsynchronizowane) | Fine-tuning OpenAI (GPT-4.1-nano) |
| 7 | 1-5 | ✅ Gotowe (zsynchronizowane) | Fine-tuning QLoRA + ewaluacja modelu (Colab GPU) |
| 8 | 1 | ✅ Gotowe (zsynchronizowane) | Modal.com + SpecialistAgent |
| 8 | 2 | ✅ Gotowe (zsynchronizowane) | RAG (ChromaDB) + FrontierAgent + EnsembleAgent |
| 8 | 3 | ✅ Gotowe (zsynchronizowane) | ScannerAgent + MessagingAgent (Pushover) |
| 8 | 4 | ✅ Gotowe (zsynchronizowane) | AutonomousPlanningAgent + pętla agentyczna |
| 8 | 5 | ✅ Gotowe (zsynchronizowane) | Finał: "The Price is Right" — UI Gradio |

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

### 🗂️ TYDZIEŃ 4 — Generowanie kodu: Python → C++ / Rust

Używanie modeli frontier LLM do tłumaczenia kodu Python na wysokowydajne języki kompilowane (C++ i Rust), benchmarkowanie wyników i owijanie wszystkiego w UI Gradio.

> **Uwaga:** Notebooki Dni 1 i 2 nie są na tej maszynie — brakuje synchronizacji. Dni 3–5 są dostępne.

---

#### Dzień 3: Generator kodu Python → C++ (porównanie 4 modeli)
**Cel:** Zbudowanie narzędzia do konwersji kodu, które tłumaczy Python na zoptymalizowany C++ i benchmarkuje przyspieszenie na rzeczywistych obliczeniach.

**Co zostało zbudowane:**
- `system_info.py` — wykrywa system operacyjny, CPU i dostępny kompilator C++
- Pipeline kompilacji: `clang++` z maksymalnymi optymalizacjami (`-Ofast -mcpu=native -flto=thin`)
- Prompt systemowy: *"przekonwertuj Python na wysokowydajny C++, odpowiadaj tylko kodem"*
- Benchmark: obliczanie π z 200 000 000 iteracjami — baseline Python: **~19,18 sekundy**

**Wyniki benchmarku (4 modele):**

| Miejsce | Model | Czas (s) | Przyspieszenie |
|---------|-------|----------|----------------|
| 4 | Claude Sonnet 4.5 | 0,104 | ~184× |
| 3 | GPT-5 | 0,082 | ~233× |
| 2 | Grok 4 | 0,018 | ~1 060× |
| 1 | Gemini 2.5 Pro | 0,013 | **~1 440×** |

---

#### Dzień 4: UI Gradio + rozszerzony benchmark 9 modeli
**Cel:** Dodanie UI Gradio do interaktywnej konwersji Python→C++ z dowolnym modelem i rozszerzenie konkurencji do 9 modeli.

**Co zostało zbudowane:**
- UI `gr.Blocks`: edytor kodu Python (lewo) → wyjście C++ (prawo), dropdown wyboru modelu
- 9 modeli z 6 dostawców: frontier (GPT-5, Claude, Grok, Gemini) + open source (Qwen, DeepSeek, gpt-oss)
- Wzorzec słownika `clients[model]` do wywoływania właściwego dostawcy

**Wyniki (ten sam benchmark π):**

| Miejsce | Model | Przyspieszenie |
|---------|-------|----------------|
| 1 | Gemini 2.5 Pro | **1 440×** |
| 2 | Grok 4 | 1 060× |
| 3 | gpt-oss-20B | 238× |
| 9 | Qwen 2.5 Coder | FAIL |

---

#### Dzień 5: Rozszerzenie Rust + trudniejszy benchmark + stylizowane UI
**Cel:** Rozszerzenie generatora kodu o Rust, dodanie trudniejszego benchmarku i dopracowanie UI Gradio.

**Co zostało zbudowane:**
- Przełącznik `language = "Rust"` / `"C++"` — prompt i rozszerzenie pliku dostosowują się automatycznie
- Pipeline kompilacji Rust: `rustc -C opt-level=3 -C target-cpu=native -C lto=fat -C panic=abort`
- **Trudniejszy benchmark:** suma podtablicy maksymalnej z generatorem LCG (wymagana obsługa dużych liczb) — wiele modeli FAILED
- `styles.py` CSS + `gr.themes.Monochrome()` + `gr.Code` z podświetlaniem składni

**Wyniki trudniejszego benchmarku:**

| Miejsce | Model | Przyspieszenie vs Python |
|---------|-------|--------------------------|
| FAIL | Gemini, Claude, GPT-5, DeepSeek, Qwen... | — |
| 3 | gpt-oss-20B | ~99 000× |
| 2 | Grok 4 | ~106 000× |
| 1 | OpenAI gpt-oss-120B | **~110 000×** |

---

### 🗂️ TYDZIEŃ 5 — RAG: Ekspert Knowledge Worker dla InsureLLM

Budowanie asystenta odpowiadającego na pytania dla fikcyjnej firmy ubezpieczeniowej (InsureLLM) — od prostego dopasowania słów kluczowych do zaawansowanego RAG z rerankingiem i przepisywaniem zapytań.

---

#### Dzień 1: RAG słownikowy (bazowy)
- Słownik Python z plikami `.md` (pracownicy, produkty, kontrakty) — klucze to nazwiska/nazwy produktów
- `get_relevant_context(message)` — dzieli wiadomość na słowa, szuka każdego w słowniku
- Chatbot `gr.ChatInterface` z `gpt-4.1-nano` — działający produkt w jednym ekranie kodu

#### Dzień 2: LangChain + ChromaDB + t-SNE
- `DirectoryLoader` + `RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)`
- Dwie opcje embeddingów: `HuggingFaceEmbeddings("all-MiniLM-L6-v2")` (darmowe, 384 dim.) vs. `OpenAIEmbeddings` (płatne)
- `Chroma.from_documents()` → trwała baza wektorów (`vector_db/`)
- Wykresy rozrzutu t-SNE 2D i 3D (Plotly) — wizualizacja klastrów typów dokumentów

#### Dzień 3: Pipeline RAG LangChain + chatbot
- `vectorstore.as_retriever()` + `ChatOpenAI(temperature=0)` + `SystemMessage`/`HumanMessage`
- `gr.ChatInterface(answer_question).launch()` — pełny chatbot w 3 liniach kodu

#### Dzień 4: Framework ewaluacji RAG
- `evaluation/tests.jsonl` — zestaw pytań z referencyjnymi odpowiedziami
- `evaluate_answer()` — sędzia LLM oceniający dokładność, kompletność i trafność
- `evaluate_retrieval()` — sprawdza czy pobrane fragmenty zawierają istotną treść

#### Dzień 5: Zaawansowany RAG
- **Chunking LLM**: model tworzy semantyczne chunki (`headline`, `summary`, `content`) zamiast dzielenia na znaki
- **Reranking**: drugi LLM reorderuje pobrane fragmenty według trafności (`RankOrder`)
- **Przepisywanie zapytań**: zapytanie użytkownika jest przepisywane na bardziej precyzyjne
- Pipeline końcowy: przepisz → pobierz → rerankuj → generuj

**Stack:** `langchain`, `chromadb`, `openai` (embeddingi), `pydantic`, `sklearn` (t-SNE), `plotly`.

---

### 🗂️ TYDZIEŃ 6 — „The Price is Right": Dane + Klasyczne ML + Sieci Neuronowe

Budowanie predyktora cen produktów od zera na bazie 820 000 zeskrapowanych opisów produktów Amazon.

---

#### Dzień 1: Kuracja danych — 820k produktów Amazon
- 8 kategorii z `McAuley-Lab/Amazon-Reviews-2023` (HuggingFace)
- Filtr cenowy $1–$1000, filtr jakości opisów
- Próbkowanie ważone ceną (820k pozycji), deduplikacja, split 80/10/10
- Wykresy: histogramy cen i długości, scatter cena vs. waga vs. długość tekstu

#### Dzień 2: Pre-processing — Groq Batch API
- Prompt systemowy: przepisanie opisów na 5-polowy format (Tytuł, Kategoria, Marka, Opis, Szczegóły)
- Pliki JSONL (1000 pozycji/plik) → `groq.batches.create()` → polowanie na wyniki
- Klasa `Batch` — hermetyzuje cały cykl: utwórz/uruchom/pobierz
- Koszt: <$1 dla Lite (20k), ~$30 dla Full (800k)

#### Dzień 3: Modele bazowe + klasyczne ML (RMSE — niżej = lepiej)

| Model | RMSE |
|-------|------|
| Stały predyktor | 106,18 |
| Regresja liniowa (3 cechy) | 101,56 |
| NLP + Regresja liniowa (BoW) | 76,81 |
| Random Forest | 72,28 |
| XGBoost | 68,23 |

#### Dzień 4: Sieć neuronowa od zera + benchmarking frontier

- **Benchmark ludzki** (100 próbek, CSV): RMSE 87,62 (gorszy niż XGBoost!)
- **8-warstwowa sieć PyTorch** (HashingVectorizer 5000 cech, 2 epoki, Adam): RMSE 63,97
- **Modele frontier zero-shot**:
  - GPT-4.1-nano: 62,51 | Grok 4.1 Fast: 57,62 | Gemini 3 Pro: 50,54
  - Claude Opus 4.5: oceniony | GPT-5.1 (`reasoning_effort="high"`): **44,74**

#### Dzień 5: Fine-tuning OpenAI (GPT-4.1-nano)
- Format JSONL: user → opis produktu, assistant → `$cena`
- `openai.fine_tuning.jobs.create()` z `gpt-4.1-nano-2025-04-14`, `n_epochs=1`
- Wyniki wg rozmiaru danych: 100 próbek → 96,58 | 2000 → 82,26 | **20 000 → 67,75**
- **Bonus — Deep Neural Network**: większa sieć trenowana 5 epok na 800k próbkach → RMSE **46,49**

**Stack:** `datasets`, `groq`, `litellm`, `sklearn`, `xgboost`, `torch`, `openai` (Files + Fine-tuning API).

---

### 🗂️ TYDZIEŃ 7 — Fine-tuning z QLoRA: „The Price is Right"

Fine-tuning **Llama 3.2-3B** na 400 000 opisach produktów Amazon do przewidywania cen produktów z tekstu — i pobicie każdego modelu frontierowego, w tym GPT-5.1.

---

#### Dzień 1: Wprowadzenie do LoRA i QLoRA
**Cel:** Zrozumienie teorii i matematyki stojącej za LoRA przed treningiem — dlaczego działa, ile pamięci oszczędza i jak czytać wagi adaptera.

**Co zostało zbadane:**
- Ładowanie Llama 3.2-3B w trzech precyzjach i porównanie śladu pamięci: pełna (~6,4 GB), 8-bit (~3,2 GB), 4-bit NF4 (~1,9 GB)
- **Matematyka LoRA:** każdy docelowy moduł otrzymuje dwie niskorangowe macierze adapterów `lora_A` i `lora_B`, wagi aktualizowane jako `base + alpha * lora_A @ lora_B`
- Tryb Lite: r=32, tylko warstwy uwagi (~13M trenowalnych parametrów z 3B łącznie)
- Tryb Full: r=256, uwaga + warstwy MLP

**Stack technologiczny:** `transformers`, `peft` (`LoraConfig`, `PeftModel`), `bitsandbytes`.

---

#### Dzień 2: Przygotowanie danych promptów + Ewaluacja modelu bazowego
**Cel:** Przekształcenie surowego datasetu Amazon w prompty do fine-tuningu i zmierzenie wydajności modelu bazowego jako punktu odniesienia.

**Co zostało zbudowane:**
- Ładowanie datasetu z HuggingFace Hub + histogram liczby tokenów (cutoff: 110 tokenów)
- `item.make_prompts(tokenizer, cutoff, include_price)` — buduje pary prompt + completion
- Wypchnięcie datasetu promptów z powrotem do HuggingFace Hub
- **Ewaluacja modelu bazowego** — RMSE: **110,72** (gorszy niż stały predyktor!)

**Stack technologiczny:** `transformers`, `datasets`, `huggingface_hub`, `matplotlib`.

---

#### Dni 3 i 4: Trening QLoRA
**Cel:** Fine-tuning Llama 3.2-3B z QLoRA używając `SFTTrainer` ze śledzeniem w Weights & Biases.

**Co zostało zbudowane:**
- Konfiguracja kwantyzacji 4-bit NF4 + konfiguracja LoRA (`LoraConfig`)
- `SFTConfig`: tryb Lite (1 epoka, batch 32, T4) lub Full (3 epoki, batch 256, A100)
- Integracja W&B: `wandb.init()` — rejestrowanie krzywych strat i metryk ewaluacji
- `SFTTrainer.train()` → `push_to_hub()` do `UserPWG/price-{timestamp}` na HuggingFace

**Stack technologiczny:** `trl` (`SFTTrainer`, `SFTConfig`), `peft`, `bitsandbytes`, `wandb`, Colab T4/A100.

---

#### Dzień 5: Ewaluacja i wyniki
**Kluczowe wyniki (RMSE — im niżej, tym lepiej):**

| Model | RMSE |
|-------|------|
| Bazowy Llama 3.2 4-bit | 110,72 |
| GPT-4.1 Nano | 62,51 |
| Fine-tuned Lite | 65,40 |
| Gemini 3 Pro | 50,54 |
| Claude 4.5 Sonnet | 47,10 |
| Deep Neural Network | 46,49 |
| GPT-5.1 | 44,74 |
| **Fine-tuned Full** | **39,85 🏆** |

**Kluczowy wniosek:** Model Fine-tuned Full (39,85 RMSE) **pobił każdy model frontierowy** łącznie z GPT-5.1. Fine-tuning domenowy na wystarczającej ilości danych wygrywa z surowym rozmiarem modelu.

---

### 🗂️ TYDZIEŃ 8 — Agentic AI: „The Price is Right"

Projekt kulminacyjny. W pełni autonomiczny system wieloagentowy, który przeszukuje internet w poszukiwaniu okazji produktowych, szacuje prawdziwą wartość produktów za pomocą wielu strategii AI i wysyła powiadomienia push na telefon — wszystko orkiestrowane przez agenta planującego w interfejsie Gradio.

**Architektura agentów:**

```
DealAgentFramework
├── ScannerAgent       — scraping stron z okazjami, GPT wybiera top 5
├── EnsembleAgent
│   ├── FrontierAgent      — RAG na 400k produktach Amazon + GPT-5.1
│   ├── SpecialistAgent    — fine-tuned Llama na Modal.com (chmura GPU)
│   └── NeuralNetworkAgent — głęboka sieć neuronowa z Tygodnia 6
├── MessagingAgent     — powiadomienia push Pushover na telefon
└── AutonomousPlanningAgent — autonomiczna pętla tool-calling sterowana LLM
```

---

#### Dzień 1: Wdrożenie w chmurze Modal.com + SpecialistAgent
**Cel:** Wdrożenie fine-tuned LLM jako produkcyjnego serwisu API na Modal.com (bezserwerowa chmura GPU), a następnie podłączenie go do pierwszego agenta.

**Co zostało zbudowane:**
- Konfiguracja konta Modal.com + token API (`modal token set`)
- `hello.py` — prosta aplikacja Modal demonstrująca lokalne vs. zdalne wykonanie
- `llama.py` — generowanie tekstu Llama wdrożone jako zdalna funkcja Modal
- `pricer_ephemeral.py` — efemeryczna aplikacja Modal: opis produktu → szacowana cena
- `pricer_service.py` / `pricer_service2.py` — trwałe **wdrożone** serwisy Modal
- Klasa `Preprocessor` — oczyszcza opisy produktów przed wysłaniem do pricera
- `SpecialistAgent` — opakowuje wdrożony pricer Modal za czystym interfejsem `.price(description)`

**Stack technologiczny:** `modal`, `agents/specialist_agent.py`, `agents/preprocessor.py`, `litellm`.

---

#### Dzień 2: Baza wektorowa RAG + FrontierAgent + EnsembleAgent
**Cel:** Zbudowanie agenta wyceny opartego na RAG nad 400 000 produktami Amazon, a następnie połączenie wszystkich strategii wyceny w ensemble.

**Co zostało zbudowane:**
- Trwała baza ChromaDB (`products_vectorstore/`) z osadzeniami 400k opisów produktów
- `sentence-transformers/all-MiniLM-L6-v2` do kodowania (wektory 384-wymiarowe)
- Redukcja wymiarów t-SNE + interaktywny wykres rozrzutu 2D/3D Plotly
- `find_similars(item)` — semantyczne wyszukiwanie 5 podobnych produktów z cenami
- **EnsembleAgent** — ważona średnia: RAG frontier (80%) + Modal specialist (10%) + sieć neuronowa (10%)
- Klasy `FrontierAgent`, `NeuralNetworkAgent`, `EnsembleAgent`

**Stack technologiczny:** `chromadb`, `sentence-transformers`, `sklearn` (t-SNE), `plotly`, `litellm`, `modal`.

---

#### Dzień 3: ScannerAgent + MessagingAgent (Pushover)
**Cel:** Zbudowanie agentów znajdujących okazje w internecie i wysyłających powiadomienia push na telefon.

**Co zostało zbudowane:**
- `ScrapedDeal.fetch()` — scraping stron agregujących okazje produktowe
- GPT-5-mini ze strukturalnym wyjściem JSON (`response_format=DealSelection`) do wyboru 5 najlepszych okazji
- `ScannerAgent` — opakowuje scraping + filtrowanie LLM w interfejs `.scan()`
- Integracja **Pushover** — powiadomienia push przez API (`https://api.pushover.net/1/messages.json`)
- `MessagingAgent` — `.push(message)` i `.notify(opis, cena, wartość, url)`

**Stack technologiczny:** `openai` (strukturalne wyjście), `requests` (Pushover API), `agents/scanner_agent.py`, `agents/messaging_agent.py`.

---

#### Dzień 4: AutonomousPlanningAgent (Pętla agentyczna)
**Cel:** Zbudowanie w pełni autonomicznego agenta, który planuje własny wieloetapowy przepływ pracy za pomocą wywołań narzędzi sterowanych przez LLM.

**Co zostało zbudowane:**
- Prototyp z 3 funkcjami-zaślepkami do zrozumienia wzorca pętli agentycznej
- Definicje narzędzi w JSON Schema dla wszystkich trzech funkcji
- **Pętla agentyczna:** `while not done: response = openai.chat.completions.create(..., tools=tools)` — LLM decyduje, które narzędzia wywołać i w jakiej kolejności
- `handle_tool_call(message)` — dynamiczne wywoływanie narzędzi przez `globals().get(tool_name)`
- **AutonomousPlanningAgent** — zamienia zaślepki na prawdziwe agenty (ScannerAgent → EnsembleAgent → MessagingAgent)
- `agent.plan()` — uruchamia pełną autonomiczną pętlę polowania na okazje

**Stack technologiczny:** `openai` (tool calling, `gpt-5.1`), `chromadb`, `agents/autonomous_planning_agent.py`.

---

#### Dzień 5: Finał — UI Gradio „The Price is Right"
**Cel:** Owinięcie całego systemu wieloagentowego w dopracowany interfejs Gradio i wydanie produktu kulminacyjnego.

**Co zostało zbudowane:**
- Iteratywna budowa UI `gr.Blocks` krok po kroku w notebooku
- Finalny layout: tabela okazji + wyświetlanie okazji + dziennik agenta na żywo
- `DealAgentFramework` — orkiestruje wszystkich agentów, zarządza `memory.json`
- `price_is_right.py` — samodzielny produkt do uruchomienia (`uv run price_is_right.py`)
- Produkt ciągle skanuje, wycenia i powiadamia — w pełni autonomiczny

**Stack technologiczny:** `gradio` (`gr.Blocks`, `gr.DataFrame`, `gr.Timer`), `deal_agent_framework.py`, pakiet `agents/`, `memory.json`.

---

### 🗂️ TYDZIEŃ 7 — Fine-tuning z QLoRA

> Notebooki Tygodnia 7 są zacommitowane (dni 1–5 + zaktualizowane warianty NEW_). Szczegółowy opis do dodania.

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
| Chmura | Google Colab (T4/A100 GPU), Modal.com (bezserwerowe GPU) |
| Agentic AI | `modal`, `chromadb`, `sentence-transformers`, API Pushover, pakiet `agents/` |
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

#### 6. **Tydzień 8 — Agentic AI ✅ UKOŃCZONE**
- Zbudowałeś pełny projekt kulminacyjny: ScannerAgent → EnsembleAgent (RAG + Modal specialist + sieć neuronowa) → MessagingAgent → AutonomousPlanningAgent → UI Gradio
- **Kluczowy wzorzec:** Pętla agentyczna `while not done` z `handle_tool_call()` jest wielokrotnie używalna dla dowolnego autonomicznego agenta
- **Modal.com to produkcyjne wdrożenie:** `modal deploy` zamienia lokalny kod w skalowalny API chmurowy — używaj tego wzorca dla każdego modelu ML, który chcesz serwować
- **Insight EnsembleAgent:** Ważenie 80/10/10 (frontier RAG / specialist / sieć neuronowa) przewyższało każdy pojedynczy model — myślenie ensemble to kluczowa umiejętność w inżynierii ML

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

*Dokument przygotowany: 27 maja 2026 | Zaktualizowany: 19 czerwca 2026 (Tygodnie 3–8 udokumentowane)*
*Document prepared: May 27, 2026 | Updated: June 19, 2026 (Weeks 3–8 documented)*
