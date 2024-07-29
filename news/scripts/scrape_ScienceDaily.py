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

# スクレイピング対象のURL
SCIENCEDAILY_AI_URL = "https://www.sciencedaily.com/news/computers_math/artificial_intelligence/"

def scrape_sciencedaily_ai_news():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(SCIENCEDAILY_AI_URL, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # ニュース記事を含む要素を取得
    articles = soup.find_all('div', class_='latest-head')

    for article in articles:
        link_tag = article.find('a')
        if not link_tag:
            print("Link tag not found")
            continue

        title = link_tag.get_text(strip=True)
        link = link_tag['href']
        
        if not link.startswith('http'):
            link = f"https://www.sciencedaily.com{link}"

        print(f"Title: {title}")  # デバッグ出力
        print(f"Link: {link}")  # デバッグ出力

        summary_tag = article.find('p')
        summary = summary_tag.get_text(strip=True) if summary_tag else ''
        print(f"Summary: {summary}")  # デバッグ出力
        
        publication_date = timezone.now()

        # DjangoのArticleモデルにデータを保存
        Article.objects.update_or_create(
            title=title,
            defaults={
                'link': link,
                'summary': summary,
                'publication_date': publication_date
            }
        )

if __name__ == "__main__":
    scrape_sciencedaily_ai_news()
    print("Scraping completed.")