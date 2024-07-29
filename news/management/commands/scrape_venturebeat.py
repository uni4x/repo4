from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from django.utils import timezone
from news.models import Article

class Command(BaseCommand):
    help = 'Scrapes VentureBeat AI news articles'

    def handle(self, *args, **kwargs):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get("https://venturebeat.com/category/ai/", headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        articles = soup.find_all('article', class_='FeaturedArticles__article')

        for article in articles:
            link_tag = article.find('a')
            if not link_tag:
                self.stdout.write(self.style.WARNING('Link tag not found'))
                continue

            title_tag = link_tag.find('h2')
            if not title_tag:
                self.stdout.write(self.style.WARNING('Title tag not found'))
                continue

            title = title_tag.get_text(strip=True)
            link = link_tag['href']
            
            if not link.startswith('http'):
                link = f"https://venturebeat.com{link}"

            summary_tag = article.find('div', class_='ArticleListing__description')
            summary = summary_tag.get_text(strip=True) if summary_tag else ''
            
            publication_date = timezone.now()

            Article.objects.update_or_create(
                title=title,
                defaults={
                    'link': link,
                    'summary': summary,
                    'publication_date': publication_date
                }
            )

        self.stdout.write(self.style.SUCCESS('Scraping completed successfully'))