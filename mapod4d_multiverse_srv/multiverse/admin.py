from django.contrib import admin

# Register your models here.

from .models import Multiverse, Metaverse, MetaverseVersion

admin.site.register(Multiverse)
admin.site.register(Metaverse)
admin.site.register(MetaverseVersion)

