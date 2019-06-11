from django.urls import path
from backend.posts.api.views import PostListAPIView


app_name='posts'

urlpatterns = [
    path('post-list/', PostListAPIView.as_view(), name='post_list'),
]