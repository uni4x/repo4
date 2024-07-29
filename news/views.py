# news/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Article, Comment, Bookmark
from .serializers import ArticleSerializer, CommentSerializer, BookmarkSerializer
from .forms import CommentForm, ArticleSearchForm, MyCustomSignupForm


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        article_id = self.request.query_params.get('article')
        if article_id:
            return Comment.objects.filter(article_id=article_id)
        # return Comment.objects.all()
        return super().get_queryset()

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        article_id = self.request.data.get('article')
        article = get_object_or_404(Article, id=article_id)
        serializer.save(user=self.request.user, article=article)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        if instance.user == self.request.user or self.request.user.is_superuser:
            instance.delete()
        else:
            raise PermissionDenied("You do not have permission to delete this comment.")


def article_list(request):
    form = ArticleSearchForm()
    query = request.GET.get('query')
    if query:
        articles = Article.objects.filter(title__icontains=query).order_by('-publication_date')
    else:
        articles = Article.objects.all().order_by('-publication_date')

    paginator = Paginator(articles, 10)  # 1ページあたりの記事数
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'news/article_list.html', {'articles': articles, 'form': form, 'page_obj': page_obj})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()
    comment_form = CommentForm()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            new_comment.save()
            return redirect('article_detail', pk=article.pk)
    
    return render(request, 'news/article_detail.html', {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    })


def custom_logout_view(request):
    logout(request)
    return redirect('/')


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



@login_required
def user_profile(request):
    bookmarks = Bookmark.objects.filter(user=request.user)
    return render(request, 'news/user_profile.html', {'bookmarks': bookmarks})