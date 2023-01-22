from django.test import TestCase
from django.urls import reverse
from softwares.models import Software
from users.models import CustomUser


class SoftwareApiTestCase(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(email='test@pippo.it', password='sdlkwelk123')
        self.software_1 = Software(
                name='soft1',
                link='https://poppo.it/file.ppp',
                description='description',
                v1=1,
                v2=2,
                v3=3,
                v4=4
        )
        self.software_1.save()
        self.software_2 = Software(
                name='soft1',
                link='https://poppo.it/file.ppp',
                description='description',
                v1=1,
                v2=3,
                v3=4,
                v4=5
        )
        self.software_2.save()


    def test_api_list_software(self):
        """ check token generation by api user login"""
        Software.objects.all()

