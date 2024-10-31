# myapp/tests/test_users.py
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from unittest.mock import patch

class UserTests(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username="testuser1", password="testpass1")
        self.user2 = User.objects.create_user(username="testuser2", password="testpass2")
        self.client.force_authenticate(user=self.user1)

    def test_get_all_users(self):
        response = self.client.get(reverse("user-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Два користувача

    def test_get_all_users_empty(self):
        with patch('django.contrib.auth.models.User.objects.all', return_value=[]):
            response = self.client.get(reverse("user-list"))
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data), 0)

    def test_create_user_with_valid_data(self):
        data = {
            "username": "newuser",
            "password": "newpass123",
            "email": "newuser@example.com"
        }
        response = self.client.post(reverse("user-list"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_with_invalid_data(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com"
            # no password field
        }
        response = self.client.post(reverse("user-list"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_missing_required_data(self):
        data = {
            "username": "newuser"
            # пропущений пароль та email
        }
        response = self.client.post(reverse("user-list"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
