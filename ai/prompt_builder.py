import json


def build_research_prompt(content, category):
    schema = {
        "summary": "",
        "key_points": [],
        "people": [],
        "organizations": [],
        "keywords": [],
        "video_hook": "",
        "thumbnail_text": ""
    }

    return f"""
You are an experienced news researcher.

Analyze the following news article and create a factual research report.

Category:
{category}

Article:

{content}

Return ONLY valid JSON.

Use this exact structure:

{json.dumps(schema, indent=4)}

Rules:
- Summary: 100-150 words
- key_points: 5 bullet points
- people: list of names
- organizations: list of companies or organizations
- keywords: SEO keywords
- video_hook: one exciting opening sentence
- thumbnail_text: maximum 5 words
"""