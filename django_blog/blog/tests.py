from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment

class CommentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)

    def test_add_comment(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('add_comment', args=[self.post.id]), {'content': 'Nice post!'})
        self.assertEqual(Comment.objects.count(), 1)

# Create your tests here.
