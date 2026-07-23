import json


def parse_response(response_text):
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        return {
            "summary": "",
            "key_points": [],
            "people": [],
            "organizations": [],
            "keywords": [],
            "video_hook": "",
            "thumbnail_text": "",
            "error": "Invalid JSON returned by AI"
        }