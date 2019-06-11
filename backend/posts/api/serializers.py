from rest_framework import serializers
from backend.posts.models import Post, gen_slug


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'author', 'created']
        read_only_fields = ('id',)


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug','content', 'author', 'created', 'modified']
        read_only_fields = ('id',)