from django.contrib import admin

# Register your models here.

from .models import Multiverse, Metaverse

admin.site.register(Multiverse)
admin.site.register(Metaverse)

