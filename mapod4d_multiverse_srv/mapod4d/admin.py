from django.contrib import admin

# Register your models here.

from .models import Mapod4d, Mapod4dVersion

admin.site.register(Mapod4d)
admin.site.register(Mapod4dVersion)

