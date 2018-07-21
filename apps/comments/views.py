from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import ImageUploadSerializer, CommentCreateSerializer


# todo 提交评论的viewset。markdown渲染
class CommentViewSet(CreateModelMixin, GenericViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = CommentCreateSerializer


# todo 图片上传功能。
class ImageUploadViewSet(CreateModelMixin, GenericViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = ImageUploadSerializer


