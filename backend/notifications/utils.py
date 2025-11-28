from .models import Notification

def create_notification(user, sender, notification_type, post=None, message=""):
    if user == sender:
        return 

    Notification.objects.create(
        user=user,
        sender=sender,
        post=post,
        notification_type=notification_type,
        message=message,
    )
