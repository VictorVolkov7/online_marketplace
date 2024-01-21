from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    """
    Serializer for user registration.
    """

    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('first_name', 'last_name', 'phone', 'email', 'password',)


class CurrentUserSerializer(serializers.ModelSerializer):
    """
    Serializer for user information.
    """

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'phone', 'email', 'image', 'role',)
