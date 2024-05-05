"""
Test for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test Models."""

    def test_create_user_with_emails_successful(self):
        """test creating a user an email successful."""
        email = 'test@example.com'
        password = 'testpassword123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
