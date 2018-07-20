from rest_framework import serializers
from .models import Comment, Image
from users.serializers import UserSerializer


class ChildrenCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    children = ChildrenCommentSerializer(many=True, read_only=True)
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        exclude = ('id', 'created_time')


class ImageUploadSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Image
        fields = ('image',)
