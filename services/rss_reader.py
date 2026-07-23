import feedparser
from services.database import create_database, save_news
from collectors.article_fetcher import fetch_article

RSS_FEEDS = {
    "Technology": "https://techcrunch.com/feed/",
    "World": "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
}


def fetch_news():

    create_database()

    for category, url in RSS_FEEDS.items():

        print(f"\nDownloading {category} News...")

        feed = feedparser.parse(url)

        for article in feed.entries[:5]:

            title = article.title
            link = article.link
            published = getattr(article, "published", "")

            print("Downloading article...")

            article_text = fetch_article(link)

            save_news(
                category,
                title,
                link,
                published,
                article_text
            )

            print("✓", title)


if __name__ == "__main__":
    fetch_news()