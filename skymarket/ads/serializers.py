from rest_framework import serializers

from .models import Comment, Ad


class AdSerializer(serializers.ModelSerializer):
    """
    Serializer for Ad.
    """
    class Meta:
        model = Ad
        fields = ('title', 'price', 'description', 'image', 'author', 'created_at')


class AdDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for Ad detail.
    """
    class Meta:
        model = Ad
        fields = ('id', 'title', 'price', 'image', 'description', 'author', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment.
    """
    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'created_at', 'ad')
