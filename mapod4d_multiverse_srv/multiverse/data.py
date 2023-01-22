from django.conf import settings


class MultiverseData():
    name = settings.MAPOD4D['multiverse']['name']

    def __str__(self):
        return self.name

