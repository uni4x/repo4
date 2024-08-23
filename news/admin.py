# news/admin.py

from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from django.core.management import call_command
from .models import Article, Comment, Bookmark

class ArticleAdmin(admin.ModelAdmin):
    change_list_template = "admin/news/article_changelist.html"
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('scrape-news/', self.scrape_news),
        ]
        return custom_urls + urls

    def scrape_news(self, request):
        call_command('scrape_all_news')
        self.message_user(request, "Successfully scraped news from all sources")
        return HttpResponseRedirect("../")

# モデルを管理画面に登録
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Bookmark)