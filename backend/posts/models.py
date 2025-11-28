from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from users.models import User

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(
        User,
        related_name="liked_posts",
        blank=True
    )

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"Post by {self.author.username}"

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on Post {self.post.id}"
