from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Notification
from .serializers import NotificationSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def my_notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by("-created_at")
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def mark_as_read(request):
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return Response({"detail": "Marked as read"})
