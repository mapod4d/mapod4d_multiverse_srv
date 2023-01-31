from django.conf import settings


class MultiverseData():
    name = settings.MAPOD4D['multiverse']['name']
    v1 = settings.MAPOD4D['multiverse']['v1']
    v2 = settings.MAPOD4D['multiverse']['v2']
    v3 = settings.MAPOD4D['multiverse']['v3']
    v4 = settings.MAPOD4D['multiverse']['v4']

    def __str__(self):
        return self.name

