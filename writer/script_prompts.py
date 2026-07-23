def build_script_prompt(research_json):
    return f"""
You are a professional YouTube news script writer.

Using the following research report, write a 3–5 minute YouTube script.

Requirements:

- Start with a powerful hook.
- Explain the story in simple English.
- Add background context.
- Explain why the news matters.
- End with a conclusion.
- Finish with:
  "If you enjoyed this video, don't forget to Like, Share and Subscribe."

Research Report:

{research_json}

Return ONLY the script.
"""