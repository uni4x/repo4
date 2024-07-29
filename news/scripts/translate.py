import os
import requests
from bs4 import BeautifulSoup
from google.cloud import translate_v2 as translate
from datetime import datetime
from django.utils import timezone
import sys
import django

# プロジェクトのルートディレクトリをパスに追加
sys.path.append('/path/to/your/django/project')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

from news.models import Article

# スクレイピング対象のURL
VENTUREBEAT_AI_URL = "https://venturebeat.com/category/ai/"

def translate_text(text, target_language='ja'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

def scrape_and_translate_news():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(VENTUREBEAT_AI_URL, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article', class_='FeaturedArticles__article')

    for article in articles:
        link_tag = article.find('a')
        if not link_tag:
            print("Link tag not found")
            continue

        title_tag = link_tag.find('h2')
        if not title_tag:
            print("Title tag not found")
            continue

        title = title_tag.get_text(strip=True)
        link = link_tag['href']
        if not link.startswith('http'):
            link = f"https://venturebeat.com{link}"

        summary_tag = article.find('div', class_='ArticleListing__description')
        summary = summary_tag.get_text(strip=True) if summary_tag else ''
        publication_date = timezone.now()

        translated_title = translate_text(title)
        translated_summary = translate_text(summary) if summary else ''

        print(f"Original Title: {title}")
        print(f"Translated Title: {translated_title}")
        print(f"Original Summary: {summary}")
        print(f"Translated Summary: {translated_summary}")

        Article.objects.update_or_create(
            title=translated_title,
            defaults={
                'link': link,
                'summary': translated_summary,
                'publication_date': publication_date
            }
        )

if __name__ == "__main__":
    scrape_and_translate_news()
    print("Scraping and translation completed.")