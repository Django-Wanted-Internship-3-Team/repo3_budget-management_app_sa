from django.test import TestCase

from budget_management.users.services import UserService


class UserServicesTest(TestCase):
    def setUp(self):
        self.user_service = UserService()

    def test_create(self):
        user = self.user_service.create(username="test", password="test1234!")
        self.assertEqual(user.username, "test")
        self.assertTrue(user.check_password("test1234!"))

    def test_create_with_duplicated_username(self):
        self.user_service.create(username="test", password="test1234!")
        with self.assertRaises(Exception):
            self.user_service.create(username="test", password="test1234!")

    def test_create_with_short_password(self):
        with self.assertRaises(Exception):
            self.user_service.create(username="test", password="test")
