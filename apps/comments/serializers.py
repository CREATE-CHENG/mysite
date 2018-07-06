from rest_framework import serializers
from .models import Comment


class ChildrenCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    children = ChildrenCommentSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
