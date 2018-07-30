from rest_framework import serializers
from .models import Article, Category
from comments.serializers import CommentSerializer


class ArticleSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        exclude = ('created_time', 'view')


class ArticleRetrieveSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Article
        fields = '__all__'


class ArticleArchiveSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format='%Y-%m')

    class Meta:
        model = Article
        fields = '__all__'


class ArticleForCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title')


class CategoryListSerializer(serializers.ModelSerializer):
    articles = ArticleForCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

