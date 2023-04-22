from django.db import models

from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db.models import F
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


from django.contrib import admin
from datetime import datetime
from projects.models import Project
from mapod4d.models import Mapod4dVersion
from .managers import MetaverseVersionManager


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
    v1 = models.PositiveIntegerField(default=0, null=False, validators=[MaxValueValidator(999)])
    v2 = models.PositiveIntegerField(default=0, null=False, validators=[MaxValueValidator(999)])
    v3 = models.PositiveIntegerField(default=0, null=False, validators=[MaxValueValidator(999)])
    v4 = models.PositiveIntegerField(default=0, null=False, validators=[MaxValueValidator(999)])
    p = models.CharField(max_length=2, default="s", null=False)    
    bricks = models.PositiveIntegerField(default=1, null=False)
    compressed = models.BooleanField(default=True, null=False)
    fmver = models.ForeignKey(to=Mapod4dVersion, on_delete=models.CASCADE, related_name="metaverseversions_from")
    tmver = models.ForeignKey(to=Mapod4dVersion, on_delete=models.CASCADE, related_name="metaverseversions_to")
    metaverse = models.ForeignKey(Metaverse, on_delete=models.CASCADE, related_name="metaverseversions")

    def get_sversion(self):
        return '{v1:03d}{v2:03d}{v3:03d}{v4:03d}'.format(
                v1=self.v1, v2=self.v2, v3=self.v3, v4=self.v4)

    class Meta:
        constraints = [
            models.UniqueConstraint('metaverse', 'v1', 'v2', 'v3', 'v4',  name='metaverse_version'),
        ]

    objects = MetaverseVersionManager()

    def clean(self):
        if self.fmver.sversion > self.tmver.sversion:
            raise ValidationError(_("fmver can be lower of tmver."))

    def __str__(self):
        name = "_".join([
                self.metaverse.mapod4d_id,
                str(self.v1),
                str(self.v2),
                str(self.v3),
                str(self.v4)
        ])
        return name

