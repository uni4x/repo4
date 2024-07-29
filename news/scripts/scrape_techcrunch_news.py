import requests
from bs4 import BeautifulSoup
from datetime import datetime
from django.utils import timezone
import os
import sys
import django

# プロジェクトのルートディレクトリをパスに追加
sys.path.append('/Users/a/Desktop/memo/Python_App/news/news_aggregator')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_aggregator.settings')
django.setup()

from news.models import Article

TECHCRUNCH_URL = "https://techcrunch.com/tag/artificial-intelligence/"

def scrape_techcrunch_news():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(TECHCRUNCH_URL, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article')

    for article in articles:
        link_tag = article.find('a')
        if not link_tag:
            print("Link tag not found")
            continue

        title = link_tag.get_text(strip=True)
        link = link_tag['href']
        
        if not link.startswith('http'):
            link = f"https://techcrunch.com{link}"

        print(f"Title: {title}")
        print(f"Link: {link}")

        summary_tag = article.find('div', class_='post-block__content')
        summary = summary_tag.get_text(strip=True) if summary_tag else ''
        print(f"Summary: {summary}")
        
        publication_date = timezone.now()

        Article.objects.update_or_create(
            title=title,
            defaults={
                'link': link,
                'summary': summary,
                'publication_date': publication_date
            }
        )

if __name__ == "__main__":
    scrape_techcrunch_news()
    print("Scraping completed.")