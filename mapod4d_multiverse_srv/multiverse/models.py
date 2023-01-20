from django.db import models

from django.core.validators import RegexValidator
from datetime import datetime

# Create your models here.


class Metaverse(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    mapod4d_id = models.CharField(max_length=50, unique=True, null=False, validators=[alphanumeric])
    link = models.URLField(default='')
    description = models.TextField(max_length=200, default='')
