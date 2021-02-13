from django.test import TestCase
from posts.models import Post

class PostModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Post.objects.create(title='Test', content='##### Hola', image='https://www.fullstackpython.com/img/logos/django.png')

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')