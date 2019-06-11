from rest_framework.generics import ListAPIView

from backend.posts.models import Post
from backend.posts.api.serializers import PostSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


