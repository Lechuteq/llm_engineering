"""Company Brochure Generator — multi-page web analysis pipeline.

Two-step LLM workflow:
1. Link curator (gpt-5-nano) — picks relevant pages (About, Careers, Products)
   from raw href list, returns structured JSON.
2. Brochure assembler (gpt-4.1-mini) — combines landing page + selected pages
   into a single markdown brochure with streaming output.

Origin: Week 1 Day 5.
"""

import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

sys.path.append(str(Path(__file__).resolve().parents[1] / "common"))
from scraper import fetch_website_contents, fetch_website_links  # noqa: E402


LINK_MODEL = "gpt-5-nano"
BROCHURE_MODEL = "gpt-4.1-mini"

LINK_SYSTEM_PROMPT = """
You are provided with a list of links found on a webpage.
You are able to decide which of the links would be most relevant to include in a brochure about the company,
such as links to an About page, or a Company page, or Careers/Jobs pages.
You should respond in JSON as in this example:

{
    "links": [
        {"type": "about page", "url": "https://full.url/goes/here/about"},
        {"type": "careers page", "url": "https://another.full.url/careers"}
    ]
}
"""

BROCHURE_SYSTEM_PROMPT = """
You are an assistant that analyzes the contents of several relevant pages from a company website
and creates a short, humorous, entertaining, witty brochure about the company for prospective customers, investors and recruits.
Respond in markdown without code blocks.
Include details of company culture, customers and careers/jobs if you have the information.
"""


def get_links_user_prompt(url: str) -> str:
    user_prompt = f"""
Here is the list of links on the website {url} -
Please decide which of these are relevant web links for a brochure about the company,
respond with the full https URL in JSON format.
Do not include Terms of Service, Privacy, email links.

Links (some might be relative links):

"""
    links = fetch_website_links(url)
    user_prompt += "\n".join(links)
    return user_prompt


def select_relevant_links(client: OpenAI, url: str) -> dict:
    print(f"→ Selecting relevant links for {url} via {LINK_MODEL}")
    response = client.chat.completions.create(
        model=LINK_MODEL,
        messages=[
            {"role": "system", "content": LINK_SYSTEM_PROMPT},
            {"role": "user", "content": get_links_user_prompt(url)},
        ],
        response_format={"type": "json_object"},
    )
    links = json.loads(response.choices[0].message.content)
    print(f"  Found {len(links.get('links', []))} relevant links")
    return links


def fetch_page_and_all_relevant_links(client: OpenAI, url: str) -> str:
    contents = fetch_website_contents(url, max_chars=2000)
    relevant_links = select_relevant_links(client, url)
    result = f"## Landing Page:\n\n{contents}\n## Relevant Links:\n"
    for link in relevant_links.get("links", []):
        result += f"\n\n### Link: {link['type']}\n"
        result += fetch_website_contents(link["url"], max_chars=2000)
    return result


def get_brochure_user_prompt(client: OpenAI, company_name: str, url: str) -> str:
    user_prompt = f"""
You are looking at a company called: {company_name}
Here are the contents of its landing page and other relevant pages;
use this information to build a short brochure of the company in markdown without code blocks.\n\n
"""
    user_prompt += fetch_page_and_all_relevant_links(client, url)
    return user_prompt[:5000]


def stream_brochure(company_name: str, url: str) -> None:
    """Print the brochure to stdout in real-time as it streams from the LLM."""
    client = OpenAI()
    user_prompt = get_brochure_user_prompt(client, company_name, url)

    print(f"\n→ Generating brochure for {company_name} via {BROCHURE_MODEL}\n")
    print("─" * 60)

    stream = client.chat.completions.create(
        model=BROCHURE_MODEL,
        messages=[
            {"role": "system", "content": BROCHURE_SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        stream=True,
    )
    for chunk in stream:
        delta = chunk.choices[0].delta.content or ""
        print(delta, end="", flush=True)

    print("\n" + "─" * 60)


def main():
    load_dotenv(override=True)
    if not os.getenv("OPENAI_API_KEY"):
        sys.exit("Error: OPENAI_API_KEY not set in environment")

    if len(sys.argv) < 3:
        company_name, url = "HuggingFace", "https://huggingface.co"
        print(f"Usage: python brochure_generator.py <company_name> <url>")
        print(f"No args provided — running demo with {company_name}\n")
    else:
        company_name, url = sys.argv[1], sys.argv[2]

    stream_brochure(company_name, url)


if __name__ == "__main__":
    main()
