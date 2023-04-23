from django.contrib import admin

# Register your models here.

from django.db.models import Value, F
from .models import Mapod4d, Mapod4dVersion

#admin.site.register(Mapod4d)
#admin.site.register(Mapod4dVersion)

@admin.register(Mapod4dVersion)
class Mapod4dVersionAdmin(admin.ModelAdmin):
    readonly_fields = ["sversion"]

    @admin.display(description="SVersion")
    def sversion(self, obj):
        return obj.sversion


class Mapod4dVersionInline(admin.StackedInline):
    model = Mapod4dVersion
    ordering = [ '-v1', '-v2', '-v3', '-v4',]
    extra = 1


@admin.register(Mapod4d)
class Mapod4dAdmin(admin.ModelAdmin):
    inlines = [
        Mapod4dVersionInline
    ]

