from django.db import models
from users.models import User
from posts.models import Post

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ("like", "Like"),
        ("comment", "Comment"),
        ("follow", "Follow"),
    )

    user = models.ForeignKey(
        User,
        related_name="notifications",
        on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        User,
        related_name="sent_notifications",
        on_delete=models.CASCADE
    )
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    message = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} → {self.user.username} ({self.notification_type})"
