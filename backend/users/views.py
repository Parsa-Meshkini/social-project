from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .serializers import UserSerializer, UserUpdateSerializer, AvatarSerializer, RegisterSerializer
from .models import User, Follow
from rest_framework import generics, permissions
from notifications.utils import create_notification

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class MeView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class MeUpdateView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = AvatarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    target = User.objects.get(id=user_id)

    if request.user == target:
        return Response({"detail": "You cannot follow yourself"}, status=400)

    Follow.objects.get_or_create(follower=request.user, following=target)

    return Response({"detail": f"You followed {target.username}"})

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    target = User.objects.get(id=user_id)

    Follow.objects.filter(follower=request.user, following=target).delete()

    return Response({"detail": f"You unfollowed {target.username}"})


@api_view(["GET"])
def followers_list(request, user_id):
    target = User.objects.get(id=user_id)

    followers = target.followers.all().values(
        "follower__id",
        "follower__username",
        "follower__avatar",
    )

    return Response(list(followers))


@api_view(["GET"])
def following_list(request, user_id):
    target = User.objects.get(id=user_id)

    following = target.following.all().values(
        "following__id",
        "following__username",
        "following__avatar",
    )

    return Response(list(following))
