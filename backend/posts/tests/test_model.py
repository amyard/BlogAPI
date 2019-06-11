from django.test import TestCase
from django.contrib.auth import get_user_model
from backend.posts.models import Post

def sample_user(username='test', password = 'zaza1234'):
    return get_user_model().objects.create_user(username, password)


class ModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(
            author=sample_user(),
            title='First Post',
            content='Here will be new content',
        )

    def test_post_check_STR(self):
        self.assertEqual(str(self.post), self.post.title)

    def test_genre_name_label(self):
        self.assertEquals(self.post._meta.get_field('title').verbose_name, 'Title')
        self.assertEquals(self.post._meta.get_field('slug').verbose_name, 'Slug')
        self.assertEquals(self.post._meta.get_field('content').verbose_name, 'Content')

    def test_post_max_length(self):
        self.assertEquals(self.post._meta.get_field('title').max_length, 255)
        self.assertEquals(self.post._meta.get_field('slug').max_length, 255)


