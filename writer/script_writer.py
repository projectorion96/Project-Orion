import json
import os

from ai.gemini_provider import ask_gemini
from writer.script_prompts import build_script_prompt


def create_script():
    # Load the research report
    with open("output/research.json", "r", encoding="utf-8") as file:
        research = json.load(file)

    # Convert the research into text for the prompt
    research_text = json.dumps(research, indent=4, ensure_ascii=False)

    # Build the prompt
    prompt = build_script_prompt(research_text)

    print("Sending research to Gemini...")

    # Ask Gemini to write the script
    script = ask_gemini(prompt)

    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    # Save the script
    with open("output/script.md", "w", encoding="utf-8") as file:
        file.write(script)

    print("✅ Script created successfully!")
    print("Saved to output/script.md")


if __name__ == "__main__":
    create_script()