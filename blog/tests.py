from django.test import TestCase
from .forms import CommentForm

class CommentFormValidationTest(TestCase):
    def test_valid_comment_submission(self):
        comment_form = CommentForm({'body': 'Excellent article, very informative'})
        self.assertTrue(comment_form.is_valid())

    def test_empty_comment_rejection(self):
        empty_comment = CommentForm({'body': ''})
        self.assertFalse(empty_comment.is_valid(), "Valid Form")
        self.assertIn('body', empty_comment.errors)
        self.assertEqual(empty_comment.errors['body'][0], 'This field is required.')
