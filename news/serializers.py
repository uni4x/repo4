# news/serializers.py

from rest_framework import serializers
from .models import Article, Comment, Bookmark

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    article = serializers.ReadOnlyField(source='article.id')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_is_owner(self, obj):
        request = self.context.get('request', None)
        if request:
            return obj.user == request.user
        return False
    

class BookmarkSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Bookmark
        fields = '__all__'