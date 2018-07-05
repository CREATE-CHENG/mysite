from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ArticleSerializer, CategorySerializer
from .models import Article, Category

class ArticlePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 1000


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = ArticlePagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category__id',)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return []
        else:
            return [IsAdminUser()]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CategoryViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_permissions(self):
        if self.action == 'create':
            return [IsAdminUser()]
        else:
            return []
