import json
import os

from models.research_model import ResearchReport


def create_research_report(title, category):

    report = ResearchReport(
        title=title,
        category=category
    )

    return report


def save_report(report):

    os.makedirs("output", exist_ok=True)

    filename = "output/research.json"

    data = {
        "title": report.title,
        "category": report.category,
        "summary": report.summary,
        "key_points": report.key_points,
        "people": report.people,
        "organizations": report.organizations,
        "keywords": report.keywords,
        "sources": report.sources
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("✅ Research report saved.")