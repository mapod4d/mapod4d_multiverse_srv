from django.contrib import admin

# Register your models here.

from .models import Project


#class CustomProjectAdmin(UserAdmin):
#    pass


admin.site.register(Project)
