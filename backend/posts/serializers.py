from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source="author.username", read_only=True)
    author_id = serializers.IntegerField(source="author.id", read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "author_id",
            "author_username",
            "text",
            "image",
            "created_at"
        ]
        read_only_fields = ["author_id", "author_username", "created_at"]


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "author", "author_username", "text", "created_at"]
        read_only_fields = ["author", "created_at"]