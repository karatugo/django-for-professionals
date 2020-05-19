from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='karatugo',
            email='karatugo@gmail.com',
            password='testpass123.'
        )

        self.assertEqual(user.username, 'karatugo')
        self.assertEqual(user.email, 'karatugo@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='superman',
            email='superman@kripton.com',
            password='testpass123.'
        )

        self.assertEqual(user.username, 'superman')
        self.assertEqual(user.email, 'superman@kripton.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)