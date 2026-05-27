"""Polish SME (Małe i Średnie Przedsiębiorstwa) Business Analyzer.

Analyzes a company website in Polish following EU SME definition guidelines.
Returns: market segment, products vs. services, target audience, competitive comparison.

Origin: Extended from Week 1 Day 1 homework.
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Make the shared scraper importable
sys.path.append(str(Path(__file__).resolve().parents[1] / "common"))
from scraper import fetch_website_contents  # noqa: E402


SYSTEM_PROMPT = (
    "Jesteś ekspertem od analizy biznesowej powiązań MŚP zgodnie z definicją UE."
)

USER_PROMPT_TEMPLATE = """
    Przeanalizuj treść strony, aby wskazać główne działania badanego podmiotu.
    Rozpoznaj na jakim rynku działa firma i co oferuje na rynek, czy są to usługi czy towary.
    Określ grupę docelowych odbiorców lub klientów do których badany podmiot kieruje swoją ofertę.
    Na koniec podaj w kilku punktach, małe podsumowanie jak wypada firma na tle podobnych jej w danej branży.

    Treść strony:
    {page_content}
"""


def analyze_company(url: str, model: str = "gpt-4.1-mini") -> str:
    """Fetch a company website and return a Polish business analysis."""
    page = fetch_website_contents(url, max_chars=5000)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_PROMPT_TEMPLATE.format(page_content=page)},
    ]

    client = OpenAI()
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content


def main():
    load_dotenv(override=True)
    if not os.getenv("OPENAI_API_KEY"):
        sys.exit("Error: OPENAI_API_KEY not set in environment")

    url = sys.argv[1] if len(sys.argv) > 1 else "https://pwginfo.pl"
    print(f"Analizuję firmę: {url}\n")
    print(analyze_company(url))


if __name__ == "__main__":
    main()
