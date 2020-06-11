from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_web_email_successful(self):
        """ Test creating new user is successful """
        email = 'test@jtdev.com'
        password = 'Testclass123'
        user = get_user_model().objects.create_user(
            email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        print("model test done")

    def test_new_user_email_normalized(self):
        """ Test that a new user email is normalized """
        email = 'test@JTDEV.com'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test new user with no email is invalid """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """ Test creating a new superuer """
        user = get_user_model().objects.create_superuser(
            'test@jtdev.com', 'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)