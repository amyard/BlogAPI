from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from backend.posts.models import Post
from backend.posts.api.serializers import PostSerializer


POST_URL = reverse('posts:post_list')
CREATE_URL = reverse('posts:post_create')


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


    # CREATE VIEW
    def test_auth_required(self):
        res = self.client.get(CREATE_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivatePostAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user('test', 'zaza1234')
        self.client.force_authenticate(self.user)

    def test_create_basic_post(self):
        payload = {
            'content': 'AWESOME CONTENT WILL BE HERE',
            'title': 'New title',
            'slug': 'new-title'
        }
        res = self.client.post(CREATE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        post = Post.objects.get(id=res.data['id'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(post, key))

    def test_create_post_without_slug(self):
        payload = {
            'content': 'AWESOME CONTENT WILL BE HERE',
            'title': 'New title'
        }
        res = self.client.post(CREATE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        post = Post.objects.get(id=res.data['id'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(post, key))

    def test_create_post_with_custom_slug(self):
        payload = {
            'content': 'AWESOME CONTENT WILL BE HERE',
            'title': 'New title'
        }
        res = self.client.post(CREATE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        post = Post.objects.get(id=res.data['id'])
        self.assertEqual(post.slug, post.title.lower().replace(' ','-'))

    def test_create_post_unique_title(self):
        user2 = get_user_model().objects.create_user('test222', 'zaza1234')
        Post.objects.create(title='Awesome 1', content='blaaaaaa blo', author=user2)

        payload = {'content':'bloooooo', 'title':'Awesome 1'}
        res = self.client.post(CREATE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)




#
# class PostPrivateAPITest(TestCase):
#
#     def setUp(self):
#         self.client = APIClient()
#         self.user = get_user_model().objects.create_user('test', 'zaza1234')
#         self.client.force_authenticate(self.user)
#
#
#     # CREATE VIEW
#     def test_create_basic_post(self):
#         payload = {
#             'content': 'AWESOME CONTENT WILL BE HERE',
#             'title': 'New title',
#             'slug': 'new-title'
#         }
#
#         res = self.client.post(CREATE_URL, payload)
#         print(res)
#         # self.assertEqual(res.status_code, status.HTTP_201_CREATED)
#         # post = Post.objects.get(id=res.data['id'])
#         # for key in payload.keys():
#         #     self.assertEqual(payload[key], getattr(post, key))
#




    #
    # # Detail View
    # def test_view_post_detail(self):
    #     '''  viewing the post detail  '''
    #     post = sample_post(user=self.user, n=1)
    #
    #     url = detail_url(post.id)
    #     res = self.client.get(url)
    #
    #     serializer = PostSerializer(post)
    #
    #     self.assertEqual(res.data, serializer.data)