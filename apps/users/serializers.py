from rest_framework import serializers
from social_django.models import UserSocialAuth
from .models import User


class SocialUserSerializer(serializers.ModelSerializer):
    extra_data = serializers.SerializerMethodField()

    class Meta:
        model = UserSocialAuth
        fields = ('extra_data',)

    def get_extra_data(self, cls):
        return {'username': cls.extra_data['username'],
                'profile_image_url': cls.extra_data['profile_image_url']}


class UserSerializer(serializers.ModelSerializer):
    social_auth = SocialUserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('social_auth',)
