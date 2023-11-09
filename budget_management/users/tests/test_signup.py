import json

from django.urls import reverse
from rest_framework.test import APITestCase

from budget_management.users.models import User


class SingupViewTest(APITestCase):
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create_user(username="test2", password="test1234!")

    def test_signup_success(self):
        response = self.client.post(
            path=reverse("signup"),
            data=json.dumps({"username": "test", "password": "test1234!"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)

    def test_signup_fail_unique_username(self):
        response = self.client.post(
            path=reverse("signup"),
            data=json.dumps({"username": "test2", "password": "test1234!"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)

    def test_signup_fail_password_validation(self):
        response = self.client.post(
            path=reverse("signup"),
            data=json.dumps({"username": "test", "password": "test"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)

    def test_signup_fail_blank_username(self):
        response = self.client.post(
            path=reverse("signup"),
            data=json.dumps({"username": "", "password": "test1234!"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)

    def test_signup_fail_blank_password(self):
        response = self.client.post(
            path=reverse("signup"),
            data=json.dumps({"username": "test", "password": ""}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)

    def test_signup_fail_required_username(self):
        response = self.client.post(
            path=reverse("signup"),
            data=json.dumps({"password": "test1234!"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)

    def test_signup_fail_required_password(self):
        response = self.client.post(
            path=reverse("signup"),
            data=json.dumps({"username": "test"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
