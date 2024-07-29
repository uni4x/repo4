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
AI_NEWS_AI_URL = "https://www.artificialintelligence-news.com/"

def scrape_ainews_ai_news():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(AI_NEWS_AI_URL, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to retrieve content: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')

    # ニュース記事を含む要素を取得
    articles = soup.find_all('article')

    for article in articles:
        header_tag = article.find('header', class_='article-header')
        if not header_tag:
            print("Header tag not found")
            continue

        link_tag = header_tag.find('a')
        if not link_tag:
            print("Link tag not found")
            continue

        title = link_tag.get_text(strip=True)
        link = link_tag['href']
        
        if not link.startswith('http'):
            link = f"https://www.artificialintelligence-news.com{link}"

        print(f"Title: {title}")  # デバッグ出力
        print(f"Link: {link}")  # デバッグ出力

        entry_content_section = article.find('section', class_='entry-content')
        if entry_content_section:
            summary_tag = entry_content_section.find('p')
            summary = summary_tag.get_text(strip=True) if summary_tag else 'No summary available'
        else:
            summary = 'No entry content available'

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
    scrape_ainews_ai_news()
    print("Scraping completed.")