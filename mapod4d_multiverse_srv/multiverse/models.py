from django.db import models

from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

from datetime import datetime
from projects.models import Project
from mapod4d.models import Mapod4dVersion

# Create your models here.


class Multiverse(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    mapod4d_id = models.CharField(max_length=50, unique=True, null=False, validators=[alphanumeric])
    server = models.URLField(default='http://infosrv0000.mapod4d.it', null=False)
    port = models.IntegerField(default='80', null=False, validators=[MinValueValidator(0), MaxValueValidator(65535)])
    description = models.TextField(max_length=200, default='')

    def __str__(self):
        return self.mapod4d_id

class Metaverse(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    mapod4d_id = models.CharField(max_length=50, unique=True, null=False, validators=[alphanumeric])
    description = models.TextField(max_length=200, default='')
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name="project_metaverses")
    multiverse = models.ForeignKey(to=Multiverse, on_delete=models.CASCADE, related_name="multiverse_metaverses")

    def __str__(self):
        return self.mapod4d_id

class MetaverseVersion(models.Model):
    link = models.URLField(default='')
    v1 = models.PositiveIntegerField(default=0, null=False)
    v2 = models.PositiveIntegerField(default=0, null=False)
    v3 = models.PositiveIntegerField(default=0, null=False)
    v4 = models.PositiveIntegerField(default=0, null=False)
    p = models.CharField(max_length=2, default="s", null=False)    
    bricks = models.PositiveIntegerField(default=1, null=False)
    compress = models.BooleanField(default=False, null=False)
    fmver = models.ForeignKey(to=Mapod4dVersion, on_delete=models.CASCADE, related_name="metaverseversions_from")
    tmver = models.ForeignKey(to=Mapod4dVersion, on_delete=models.CASCADE, related_name="metaverseversions_to")
    metaverse = models.ForeignKey(Metaverse, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint('metaverse', 'fmver', 'tmver', name='metaverse_version_range'),
            models.UniqueConstraint('metaverse', 'fmver', name='metaverse_version_fromver'),
            models.UniqueConstraint('metaverse', 'tmver', name='metaverse_version_tover'),
            models.UniqueConstraint('metaverse', 'v1', 'v2', 'v3', 'v4',  name='metaverse_version'),
#            CheckConstraint(check=Q(fromver__value=18), name='version_range')
        ]

    def __str__(self):
        name = "_".join([
                self.metaverse.mapod4d_id,
                self.v1,
                self.v2,
                self.v3,
                self.v4
        ])
        return name

