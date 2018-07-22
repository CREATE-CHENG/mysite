from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import ImageUploadSerializer, CommentCreateSerializer


class CommentViewSet(CreateModelMixin, GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = CommentCreateSerializer


class ImageUploadViewSet(CreateModelMixin, GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = ImageUploadSerializer


