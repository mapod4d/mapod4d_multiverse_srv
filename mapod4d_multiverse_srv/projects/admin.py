from django.contrib import admin

# Register your models here.

from .models import Project
from multiverse.admin import MetaverseInline


#class CustomProjectAdmin(UserAdmin):
#    pass


#admin.site.register(Project)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        MetaverseInline
    ]

