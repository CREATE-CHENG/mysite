from rest_framework import serializers
from .models import Article, Category
from comments.serializers import CommentSerializer


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        exclude = ('id', 'created_time', 'view')


class ArticleRetrieveSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    created_time = serializers.DateTimeField(format='%Y-%m-%d: %H:%M')

    class Meta:
        model = Article
        fields = '__all__'


class ArticleArchiveSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format='%Y-%m')

    class Meta:
        model = Article
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_count(self, obj):
        return obj.articles.count()


class CategoryWithArticleSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'
