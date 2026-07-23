from database.story_repository import get_top_story
from research.researcher import create_research_report
from research.researcher import save_report


story = get_top_story()

if story:

    title, category = story

    report = create_research_report(
        title,
        category
    )

    save_report(report)

else:

    print("No stories found.")