#from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api_backend.api_app.models import User

class UserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('api/register')
        data = {'username': 'DabApps',
                'email': 'DabApps@gmail.com',
                'password': '123',
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'DabApps')
        self.assertEqual(User.objects.get().email, 'DabApps@gmail.com')