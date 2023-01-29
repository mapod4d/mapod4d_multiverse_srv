from users.models import CustomUser



class Mapod4dDbBase:

    def mapod4dDbInit(self):
        self.user = CustomUser.objects.create_user(email='test@pippo.it', password='sdlkwelk123')
        self.user = CustomUser.objects.create_user(email='test1@pippo.it', password='1sdlkwelk123')
        self.user = CustomUser.objects.create_user(email='test2@pippo.it', password='2sdlkwelk123')

