from django.urls import path
from .views import *

urlpatterns = [
    path("", my_notifications),
    path("read/", mark_as_read),
]
