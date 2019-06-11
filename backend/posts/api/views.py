from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from backend.posts.models import Post
from backend.posts.api.serializers import PostSerializer, PostCreateSerializer
from backend.posts.api.permissions import IsOwnerOrReadOnly

# from backend.posts.models import gen_slug
#
# class PostViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get_queryset(self):
#         return self.queryset.order_by('-id')
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)



class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication, )


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )