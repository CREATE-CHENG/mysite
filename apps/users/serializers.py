from rest_framework import serializers
from social_django.models import UserSocialAuth
from .models import User


class SocialUserSerializer(serializers.ModelSerializer):
    extra_data = serializers.SerializerMethodField()

    class Meta:
        model = UserSocialAuth
        fields = ('extra_data',)

    def get_extra_data(self, cls):
        return {'profile_image_url': cls.first().extra_data['profile_image_url']}


class UserSerializer(serializers.ModelSerializer):
    social_auth = SocialUserSerializer()

    class Meta:
        model = User
        fields = ('social_auth', 'first_name')
