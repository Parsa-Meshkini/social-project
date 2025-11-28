from rest_framework import generics, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from notifications.utils import create_notification

class CreatePostView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()


class UserPostsView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author_id=self.kwargs['user_id'])


class DeletePostView(generics.DestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found"}, status=404)

    post.likes.add(request.user)
    return Response({"detail": "Liked!"}, status=200)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def unlike_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found"}, status=404)

    post.likes.remove(request.user)
    return Response({"detail": "Unliked!"}, status=200)


@api_view(["GET"])
def post_likes(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found"}, status=404)

    users = post.likes.all().values("id", "username")
    return Response({"likes": users, "count": post.total_likes()})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_comment(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found"}, status=404)

    text = request.data.get("text")

    if not text:
        return Response({"detail": "Text is required"}, status=400)

    comment = Comment.objects.create(
        post=post,
        author=request.user,
        text=text
    )
    return Response(CommentSerializer(comment).data, status=201)


@api_view(["GET"])
def list_comments(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found"}, status=404)

    comments = post.comments.all().order_by("-created_at")
    return Response(CommentSerializer(comments, many=True).data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_comment(request, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return Response({"detail": "Comment not found"}, status=404)

    if comment.author != request.user:
        return Response({"detail": "Not allowed"}, status=403)

    comment.delete()
    return Response({"detail": "Comment deleted"})
