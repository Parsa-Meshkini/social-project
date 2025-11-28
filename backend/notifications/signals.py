from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from posts.models import Post, Comment
from notifications.models import Notification
from django.db.models.signals import post_save
from users.models import Follow, User

User = get_user_model()

# --------------------------
# FOLLOW NOTIFICATIONS
# --------------------------
@receiver(post_save, sender=Follow)
def notify_on_follow(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.following,              # who receives notification
            sender=instance.follower,             # who triggered it
            notification_type="follow",
            message=f"{instance.follower.username} started following you"
        )
# --------------------------
# LIKE NOTIFICATIONS
# --------------------------
@receiver(m2m_changed, sender=Post.likes.through)
def create_like_notification(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        for liker_id in pk_set:
            if liker_id != instance.author.id:
                Notification.objects.create(
                    recipient=instance.author,
                    actor_id=liker_id,
                    verb="liked your post",
                    target_type="post",
                    target_id=instance.id,
                )

# --------------------------
# COMMENT NOTIFICATIONS
# --------------------------
@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        if instance.user != post.author:
            Notification.objects.create(
                recipient=post.author,
                actor=instance.user,
                verb="commented on your post",
                target_type="post",
                target_id=post.id,
            )
