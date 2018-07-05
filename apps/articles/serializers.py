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


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
