# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an **LLM Engineering** educational course repository that teaches practical AI/ML engineering over 8 weeks. The course covers building with LLMs, from foundational concepts through advanced agentic AI systems.

## Project Structure

- **week1-week8/**: Each week contains 4-5 day-based Jupyter notebooks (day1.ipynb through day5.ipynb) with lessons and exercises
  - Each week may have supporting Python scripts, evaluation frameworks, and knowledge base resources
  - `community-contributions/` folders in each week contain solutions from students
  - Some weeks (e.g., week5) have `implementation/` and `evaluation/` subdirectories
- **guides/**: 14 standalone guide notebooks covering foundational topics (Git, Python, async, APIs, Docker, etc.)
- **setup/**: Installation and environment setup instructions for all platforms

## Development Setup

### Environment Configuration

The project supports two dependency management approaches:

**Option 1: UV (faster, recommended)**
```bash
uv sync
uv run jupyter lab
```

**Option 2: Conda/Anaconda**
```bash
conda env create -f environment.yml
conda activate llms
jupyter lab
```

**Python Version**: 3.11 or 3.12 (specified in `.python-version`)

### API Keys & Environment

API keys are stored in `.env` file (ignored by Git). Required for:
- `OPENAI_API_KEY` - OpenAI models
- `ANTHROPIC_API_KEY` - Claude models
- `GOOGLE_API_KEY` - Google Gemini
- `GROQ_API_KEY`, `DEEPSEEK_API_KEY`, `GROK_API_KEY`, `OPENROUTER_API_KEY` - Alternative providers
- `HF_TOKEN` - Hugging Face models
- `JWT_SECRET` - For demo applications

The course uses minimal API spending. To keep costs low:
- OpenAI: Use `gpt-4-1-nano` (or latest nano model)
- Anthropic: Use `claude-3-haiku-20240307` (or latest haiku)
- Ollama: Use for free local inference when possible

## Running the Course Content

### Jupyter Notebooks

All learning content is in Jupyter notebooks. To work through a week:

```bash
jupyter lab week1/day1.ipynb
```

**Key points**:
- Read and execute cells sequentially
- Inspect objects and variables to understand what's happening
- Don't just run all cells at once; pause and experiment
- The course emphasizes learning by doing—modify code and test your changes

### Gradio Applications

Some weeks (particularly week5+) include Gradio-based UI applications:
```bash
python week5/app.py
```

This launches an interactive web interface for demonstrations and exercises.

## Key Technologies & Libraries

### LLM & AI Providers
- **langchain** - Framework for building LLM applications (LLMs, chains, RAG)
- **langchain-openai**, **langchain-anthropic**, **langchain-community** - Provider integrations
- **openai** - OpenAI API client
- **anthropic** - Claude API client
- **google-generativeai**, **google-genai** - Google Gemini
- **ollama** - Local open-source LLM inference
- **groq** - Fast inference API
- **litellm** - Unified LLM API wrapper

### Vector Databases & Embeddings
- **chromadb** - Vector database for RAG
- **langchain-chroma** - Chroma integration for langchain
- **sentence-transformers** - Generate embeddings from text

### Data & ML
- **transformers** - HuggingFace models (NLP, image)
- **torch** - PyTorch deep learning
- **datasets** - HuggingFace datasets (version pinned at 3.6.0)
- **pandas**, **numpy**, **scipy** - Data manipulation
- **scikit-learn** - Machine learning utilities
- **wandb** - ML experiment tracking

### Frontend & Visualization
- **gradio** - Build simple web UIs for ML
- **jupyter-dash**, **plotly** - Interactive visualizations
- **ipywidgets**, **ipykernel** - Interactive notebook widgets

### Audio & Utilities
- **pydub** - Audio processing
- **beautifulsoup4** - Web scraping
- **feedparser** - RSS feed parsing
- **requests** - HTTP library
- **tqdm** - Progress bars
- **modal** - Cloud execution

## Common Development Tasks

### Running a Single Notebook Cell

Open the notebook in Jupyter Lab and execute cells one at a time. Use Shift+Enter to run a cell and move to the next.

### Testing Code Changes

1. Modify Python code in notebook cells or in `.py` files in the week directory
2. Execute the cell to test immediately
3. Inspect variables in the notebook to verify behavior

### Working with Exercises

Each week typically has a "week X EXERCISE.ipynb" file:
1. Follow the prompts in the notebook
2. Write your solution in the designated cells
3. You can compare with community solutions in `community-contributions/` or check `solutions/` folder

### Debugging

The guides/ folder includes `08_debugging.ipynb` for detailed debugging techniques. Key approaches:
- Use print() statements in notebooks
- Use the debugger in JupyterLab (Debug menu)
- Inspect variable state at each step
- Use `type()`, `len()`, `shape` to understand data structures

## Course Philosophy

The course emphasizes **learning by doing**:
- Work through notebooks step-by-step, don't skip ahead
- Run each cell and understand the output
- Modify code and experiment—there's no penalty for trying things
- The challenges are designed to be educational, not just toy projects
- Submit PRs to share your solutions with the community

## Important Notes

- **Week 3+**: Some content uses Google Colab for GPU access (optional for paid tier, but free tier available)
- **Llama models**: Use llama3.2 or llama3.2:1b locally. Avoid llama3.3 (too large for most machines)
- **Community contributions**: High-quality student solutions are available in each week's `community-contributions/` folder
- **API costs**: All course projects should cost < $2 total if using the recommended cheaper models
- **No need to memorize**: The guides/ folder includes reference notebooks you can return to

## External Resources

- Course slides and resources: https://edwarddonner.com/2024/11/13/llm-engineering-resources/
- Instructor: Ed Donner (ed@edwarddonner.com)
- Setup help: See setup/SETUP-new.md for detailed environment configuration by platform
