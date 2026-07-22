from services.rss_reader import fetch_news
from services.ranking_engine import rank_articles

def main():
    print("=" * 60)
    print("🚀 PROJECT ORION")
    print("=" * 60)

    print("\nStep 1: Collecting news...")
    fetch_news()

    print("\nStep 2: Ranking stories...")
    rank_articles()

    print("\n✅ Pipeline completed successfully!")

if __name__ == "__main__":
    main()