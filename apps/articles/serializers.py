from rest_framework import serializers
from .models import Article, Category


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        exclude = ('id', 'created_time', 'view')


class ArticleArchiveSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format='%Y-%m')

    class Meta:
        model = Article
        fields = ('id', 'created_time', 'view', 'title')


class CategorySerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'count')


class CategoryWithArticleSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'

