from django.urls import path
from backend.posts.api.views import PostListAPIView, PostDetailView


app_name='posts'

urlpatterns = [
    path('post-list/', PostListAPIView.as_view(), name='post_list'),
    path('post-list/<str:pk>', PostDetailView.as_view(), name='post_detail'),
]