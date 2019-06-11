from rest_framework import serializers
from backend.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'author', 'created']
        read_only_fields = ('id',)