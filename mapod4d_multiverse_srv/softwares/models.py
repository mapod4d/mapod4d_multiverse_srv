from django.db import models

from django.core.validators import RegexValidator, MaxValueValidator
from .managers import SoftwareManager

# Create your models here.

class Software(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    name = models.CharField(max_length=15, null=False, validators=[alphanumeric])
    link = models.URLField(default='')
    v1 = models.PositiveIntegerField(default=0, null=False, validators=[MaxValueValidator(999)])
    v2 = models.PositiveIntegerField(default=0, null=False, validators=[MaxValueValidator(999)])
    v3 = models.PositiveIntegerField(default=0, null=False, validators=[MaxValueValidator(999)])
    v4 = models.PositiveIntegerField(default=0, null=False, validators=[MaxValueValidator(999)])
    bricks = models.PositiveIntegerField(default=1, null=False)
    compressed = models.BooleanField(default=True, null=False)
    description = models.TextField(max_length=200, default='')

    objects = SoftwareManager()

    def get_sversion(self):
        return '{v1:03d}{v2:03d}{v3:03d}{v4:03d}'.format(
                v1=self.v1, v2=self.v2, v3=self.v3, v4=self.v4)

    class Meta:
        constraints = [
            models.UniqueConstraint('name', 'v1', 'v2', 'v3', 'v4',  name='software_version'),
        ]

    def __str__(self):
        name = "_".join([
                self.name,
                str(self.v1),
                str(self.v2),
                str(self.v3),
                str(self.v4)
        ])
        return name


