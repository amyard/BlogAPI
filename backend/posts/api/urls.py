from django.urls import path
from backend.posts.api.views import PostListAPIView, PostCreateAPIView


app_name='posts'

urlpatterns = [
    path('', PostListAPIView.as_view(), name='post_list'),
    path('create/', PostCreateAPIView.as_view(), name='post_create'),
    # path('post-list/<str:pk>', PostDetailView.as_view(), name='post_detail'),
]