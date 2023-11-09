from django.test import TestCase

from budget_management.users.models import User
from budget_management.users.selectors import get_user_by_username


class UserSelectorsTest(TestCase):
    def setUp(self):
        User.objects.create_user(username="test", password="test1234!")
        self.user = get_user_by_username("test")

    def test_get_user_by_username(self):
        self.assertEqual(self.user.username, "test")

    def test_get_user_by_username_not_found(self):
        user = get_user_by_username("test2")
        self.assertIsNone(user)
