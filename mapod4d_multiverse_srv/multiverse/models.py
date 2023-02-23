from django.db import models

from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

from datetime import datetime
from projects.models import Project

# Create your models here.


class Multiverse(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    mapod4d_id = models.CharField(max_length=50, unique=True, null=False, validators=[alphanumeric])
    server = models.URLField(default='http://infosrv0000.mapod4d.it', null=False)
    port = models.IntegerField(default='80', null=False, validators=[MinValueValidator(0), MaxValueValidator(65535)])
    description = models.TextField(max_length=200, default='')

    def __str__(self):
        return "" + self.mapod4d_id


class Metaverse(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    mapod4d_id = models.CharField(max_length=50, unique=True, null=False, validators=[alphanumeric])
    link = models.URLField(default='')
    description = models.TextField(max_length=200, default='')
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name="metaverses")
    v1 = models.PositiveIntegerField(default=0, null=False)
    v2 = models.PositiveIntegerField(default=0, null=False)
    v3 = models.PositiveIntegerField(default=0, null=False)
    v4 = models.PositiveIntegerField(default=0, null=False)
    bricks = models.PositiveIntegerField(default=1, null=False)
    compress = models.BooleanField(default=False, null=False)
    frommv1 = models.PositiveIntegerField(default=0, null=False)
    frommv2 = models.PositiveIntegerField(default=0, null=False)
    frommv3 = models.PositiveIntegerField(default=0, null=False)
    frommv4 = models.PositiveIntegerField(default=0, null=False)
    tomv1 = models.PositiveIntegerField(default=0, null=False)
    tomv2 = models.PositiveIntegerField(default=0, null=False)
    tomv3 = models.PositiveIntegerField(default=0, null=False)
    tomv4 = models.PositiveIntegerField(default=0, null=False)

    def __str__(self):
        return self.mapod4d_id
