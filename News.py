import requests


def news():
    """Fetches latest news from News API."""
    api_key = "https://newsapi.org/v2/everything?q=tesla&from=2024-09-24&sortBy=publishedAt&apiKey=7163fdcb0d794b6d93da7fee862d2618"  # Replace with actual API key
    url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-09-24&sortBy=publishedAt&apiKey=7163fdcb0d794b6d93da7fee862d2618"
    response = requests.get(url)
    news_data = response.json()
    articles = news_data.get('articles', [])
    news_list = [article['title'] for article in articles]
    return news_list

