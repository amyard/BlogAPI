from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from backend.posts.models import Post
from backend.posts.api.serializers import PostSerializer, PostCreateSerializer

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


# class PostDetailView(RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     # lookup_field='slug'
#
# class PostUpdateView(UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

    # def perform_update(self, serializer):
    #     instance = self.get_object()
    #     serializer.save(slug=gen_slug(instance.title))



# from rest_framework import viewsets, mixins
#
# class PostViewSet(viewsets.ModelViewSet):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#
#     def get_queryset(self):
#         return self.queryset.all().order_by('-id')
#
#     def get_serializer_class(self):
#         '''  return needed serializer class  '''
#         if self.action == 'create':
#             return PostDetailSerializer
#         return self.serializer_class
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user, )