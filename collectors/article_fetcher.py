from newspaper import Article


def fetch_article(url):
    """
    Downloads and extracts the main article text.
    Returns None if extraction fails.
    """

    try:
        article = Article(url)

        article.download()
        article.parse()

        return article.text

    except Exception as e:
        print(f"Failed: {e}")
        return None