from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", MeView.as_view(), name="me"),
    path("me/update/", MeUpdateView.as_view(), name="me_update"),
    path("me/avatar/", AvatarUpdateView.as_view(), name="avatar_update"),
    path("<int:user_id>/follow/", follow_user),
    path("<int:user_id>/unfollow/", unfollow_user),
    path("<int:user_id>/followers/", followers_list),
    path("<int:user_id>/following/", following_list),
]
