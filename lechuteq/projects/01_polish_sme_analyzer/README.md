# 01 — Polish SME Business Analyzer

## 🇬🇧 English

**Goal:** Analyze a company website in Polish according to EU SME (Small and Medium Enterprise) definition guidelines. Returns market segment, products vs. services classification, target audience, and a competitive comparison.

**Origin:** Custom homework extension from Week 1 Day 1.

**Tech stack:** Python 3.12, `openai`, `beautifulsoup4`, `requests`, `python-dotenv`.

**Run:**
```bash
# Default (analyzes pwginfo.pl)
uv run python sme_analyzer.py

# Custom URL
uv run python sme_analyzer.py https://company-website.pl
```

**Output:** Markdown-formatted business analysis in Polish.

---

## 🇵🇱 Polski

**Cel:** Analiza strony firmowej w języku polskim zgodnie z definicją UE dla MŚP. Zwraca segment rynkowy, klasyfikację produkty vs. usługi, grupę docelową i porównanie konkurencyjne.

**Pochodzenie:** Własne rozszerzenie pracy domowej z Tygodnia 1, Dnia 1.

**Stack technologiczny:** Python 3.12, `openai`, `beautifulsoup4`, `requests`, `python-dotenv`.

**Uruchomienie:**
```bash
# Domyślnie (analizuje pwginfo.pl)
uv run python sme_analyzer.py

# Własny URL
uv run python sme_analyzer.py https://strona-firmy.pl
```

**Wynik:** Analiza biznesowa w formacie Markdown w języku polskim.
