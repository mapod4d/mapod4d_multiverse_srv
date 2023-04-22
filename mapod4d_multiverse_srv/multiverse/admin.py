from django.contrib import admin

# Register your models here.

from .models import Multiverse, Metaverse, MetaverseVersion

admin.site.register(Multiverse)
admin.site.register(Metaverse)
#admin.site.register(MetaverseVersion)

@admin.register(MetaverseVersion)
class MetaverseVersionAdmin(admin.ModelAdmin):
    readonly_fields = ["sversion"]

    @admin.display(description="SVersion")
    def sversion(self, obj):
        return obj.sversion


