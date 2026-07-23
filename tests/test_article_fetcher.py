from collectors.article_fetcher import fetch_article

url = "https://techcrunch.com/"

text = fetch_article(url)

print("=" * 60)

if text:
    print(text[:1000])
else:
    print("No article extracted.")