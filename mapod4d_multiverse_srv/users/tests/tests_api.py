from django.test import TestCase
from django.urls import reverse
from users.models import CustomUser


class UserApiTestCase(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@pippo.it', password='sdlkwelk123')


    def test_api_user_login(self):
        """ check token generation by api user login"""
        data = {
            "username": "test@pippo.it",
            "password": "sdlkwelk123"
        }
        response = self.client.post(reverse('knox_login'), data, format='json')
        # print(response.status_code, response.content)
        self.assertEqual(response.status_code, 200)

