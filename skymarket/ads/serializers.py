from rest_framework import serializers

from users.serializers import CurrentUserSerializer
from .models import Comment, Ad


class AdSerializer(serializers.ModelSerializer):
    """
    Serializer for Ad.
    """
    class Meta:
        model = Ad
        fields = ('id', 'title', 'price', 'description', 'image', 'author', 'created_at')


class AdDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for Ad detail.
    """
    author = CurrentUserSerializer(read_only=True)

    class Meta:
        model = Ad
        fields = ('id', 'title', 'price', 'image', 'description', 'author', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment.
    """
    author = CurrentUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'created_at', 'ad')


# DRF-spectacular serializers
class CommonDetailSerializer(serializers.Serializer):
    """
    Serializer for DRF-spectacular documentation.
    Used to process status codes.
    """
    detail = serializers.CharField()


class CommonDetailAndStatusSerializer(serializers.Serializer):
    """
    Serializer for DRF-spectacular documentation.
    Used to process status codes.
    """
    status = serializers.IntegerField()
    details = serializers.CharField()
