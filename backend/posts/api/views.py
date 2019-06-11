from rest_framework.generics import ListAPIView, RetrieveAPIView

from backend.posts.models import Post
from backend.posts.api.serializers import PostSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # lookup_field='slug'

