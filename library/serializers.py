from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        ordering = ['-date_joined']
        fields = ['username', 'email', 'is_staff', 'is_active', 'date_joined', 'last_login']
        read_only_fields = ['date_joined', 'last_login']


class UserRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']