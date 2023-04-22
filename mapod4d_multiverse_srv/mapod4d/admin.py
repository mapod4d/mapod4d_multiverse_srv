from django.contrib import admin

# Register your models here.

from django.db.models import Value, F
from .models import Mapod4d, Mapod4dVersion

admin.site.register(Mapod4d)
#admin.site.register(Mapod4dVersion)

@admin.register(Mapod4dVersion)
class Mapod4dVersionAdmin(admin.ModelAdmin):
    readonly_fields = ["sversion"]

    @admin.display(description="SVersion")
    def sversion(self, obj):
        return obj.sversion


