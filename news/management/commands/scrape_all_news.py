# news/management/commands/scrape_all_news.py

from django.core.management.base import BaseCommand
from news.scripts.scrape_techcrunch_news import scrape_techcrunch_news
from news.scripts.scrape_ScienceDaily import scrape_sciencedaily_ai_news
from news.scripts.scrape_ainews import scrape_ainews_ai_news
from news.scripts.scrape_VentureBeatAI_news import scrape_venturebeat_ai_news

class Command(BaseCommand):
    help = 'Scrape news from various sources'

    def handle(self, *args, **kwargs):
        scrape_techcrunch_news()
        scrape_sciencedaily_ai_news()
        scrape_ainews_ai_news()
        scrape_venturebeat_ai_news()
        self.stdout.write(self.style.SUCCESS('Successfully scraped news from all sources'))