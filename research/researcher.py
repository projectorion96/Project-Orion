import json
import os

from database.story_repository import get_top_story
from ai.prompt_builder import build_research_prompt
from ai.gemini_provider import ask_gemini
from ai.response_parser import parse_response


def create_research_report():
    story = get_top_story()

    if not story:
        print("No story found.")
        return

    title, category, article_text = story

    # Use the full article if available; otherwise fall back to the title.
    if article_text:
        prompt = build_research_prompt(article_text, category)
    else:
        prompt = build_research_prompt(title, category)

    print("Sending story to Gemini...")

    response = ask_gemini(prompt)

    report = parse_response(response)

    report["title"] = title
    report["category"] = category

    os.makedirs("output", exist_ok=True)

    with open("output/research.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print("Research report created successfully.")


if __name__ == "__main__":
    create_research_report()