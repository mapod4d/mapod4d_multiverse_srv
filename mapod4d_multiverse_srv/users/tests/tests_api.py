from django.test import TestCase
from django.urls import reverse
from users.models import CustomUser
from tests.support_tests import Mapod4dDbBase

import json


class UserApiTestCase(TestCase, Mapod4dDbBase):

    def setUp(self):
        #self.user = CustomUser.objects.create_user(email='test@pippo.it', password='sdlkwelk123')
        self.mapod4dDbInit()


    def test_api_user_login(self):
        """ check token generation by api user login"""
        data = {
            "username": "test@pippo.it",
            "password": "sdlkwelk123"
        }
        response = self.client.post(reverse('knox_login'), data, format='json')
        self.assertEqual(response.status_code, 200)
        #print(response.content)
        json_response = json.loads(response.content)
        self.assertEqual('token' in json_response, True)
        #print(json_response['token'])


    def test_api_user_bad_login(self):
        """ check invalid user api user login"""
        data = {
            "username": "test@pippo.it",
            "password": "errorpass"
        }
        response = self.client.post(reverse('knox_login'), data, format='json')
        self.assertEqual(response.status_code, 400)
        json_response = json.loads(response.content)
        self.assertEqual('token' in json_response, False)


    def test_api_user_logout(self):
        """ check user api user logout"""
        data = {
            "username": "test@pippo.it",
            "password": "sdlkwelk123"
        }
        response = self.client.post(reverse('knox_login'), data, format='json')
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content)
        self.assertEqual('token' in json_response, False)
        print("DA FINIRE")

