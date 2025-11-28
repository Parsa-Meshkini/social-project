from django.urls import path
from .views import *

urlpatterns = [
    path("create/", CreatePostView.as_view()),
    path("feed/", FeedView.as_view()),
    path("user/<int:user_id>/", UserPostsView.as_view()),
    path("<int:pk>/delete/", DeletePostView.as_view()),
    #---Likes
    path("<int:post_id>/like/", like_post),
    path("<int:post_id>/unlike/", unlike_post),
    path("<int:post_id>/likes/", post_likes),
    #---Comments
    path("<int:post_id>/comments/create/", create_comment),
    path("<int:post_id>/comments/", list_comments),
    path("comments/<int:comment_id>/delete/", delete_comment),
]
