from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from backend.posts.models import Post
from backend.posts.api.serializers import PostSerializer


POST_URL = reverse('posts:post_list')



def sample_post(user, n, **params):
    defaults = {
        'title': f'New title for post {n}',
        'content': 'New content will be here. Someday. Maybe.'
    }
    defaults.update(**params)
    return Post.objects.create(author=user, **defaults)


def detail_url(post_id):
    '''  RETURN POST DETAIL URL   '''
    return reverse('posts:post_detail', args=[post_id])



class PostAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user('test', 'zaza1234')

    # List View
    def test_retrive_post(self):
        '''   Retrieve all posts  '''
        sample_post(user=self.user, n=1)
        sample_post(user=self.user, n=2)

        res = self.client.get(POST_URL)

        posts = Post.objects.all().order_by('-id')
        serializer = PostSerializer(posts, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


    def test_posts_limited_to_user(self):
        '''   retrieving posts for specific user '''
        user2 = get_user_model().objects.create_user('bla', 'pass1234')

        sample_post(user=self.user, n=1)
        sample_post(user=user2, n=2)

        res = self.client.get(POST_URL)

        posts = Post.objects.filter(author=user2)
        serializer = PostSerializer(posts, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(posts.count(), 1)

    # Detail View
    def test_view_post_detail(self):
        '''  viewing the post detail  '''
        post = sample_post(user=self.user, n=1)

        url = detail_url(post.id)
        res = self.client.get(url)

        serializer = PostSerializer(post)

        self.assertEqual(res.data, serializer.data)