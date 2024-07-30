# news/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, CommentViewSet, BookmarkViewSet, article_list, article_detail, custom_logout_view, user_profile, translate_text

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'bookmarks', BookmarkViewSet)

urlpatterns = [
    path('', article_list, name='home'),
    path('articles/', article_list, name='article_list'),
    path('articles/<int:pk>/', article_detail, name='article_detail'),
    path('api/', include(router.urls)),
    path('logout/', custom_logout_view, name='custom_logout'),
    path('profile/', user_profile, name='user_profile'),
    path('translate/translate/', translate_text, name='translate_text'),
]