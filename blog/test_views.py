from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post

class BlogViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username = "testSuper",
            password = "Password",
            email = "tester@testing.com"
        )
        self.post = Post(
            title="Test Title", author=self.user,
            slug="test-blog-title", excerpt = "Test Blog Excerpt",
            content ="Test Blog Content", status=1)
        self.post.save()

    def test_post_full_with_comment_form(self):

        response = self.client.get(reverse('post_full', args=['test-blog-title']))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Title", response.content)
        self.assertIn(b"Test Blog Content", response.content)
        self.assertIsInstance(response.context['comment_form'], CommentForm)

    def test_successful_comment_submission(self):
        self.client.login(
            username="testSuper",
            password="Password",
        )

        post_data = {
    'body': 'Comment for test.'
}

response = self.client.post(reverse(
    'post_full', args=['blog']), post_data)

    self.assertEqual(response.status_code, 200)