from django.db import models

from users.models import CustomUser

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    description = models.CharField(max_length=250)
    users = models.ManyToManyField(to=CustomUser, related_name="projects")

    def __str__(self):
        return self.name

