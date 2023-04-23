from django.contrib import admin

# Register your models here.

from .models import Multiverse, Metaverse, MetaverseVersion

#admin.site.register(Multiverse)
#admin.site.register(Metaverse)
#admin.site.register(MetaverseVersion)


@admin.register(MetaverseVersion)
class MetaverseVersionAdmin(admin.ModelAdmin):
    readonly_fields = ["sversion"]

    @admin.display(description="SVersion")
    def sversion(self, obj):
        return obj.sversion


class MetaverseVersionInline(admin.StackedInline):
    model = MetaverseVersion
    ordering = [ '-v1', '-v2', '-v3', '-v4',]
    extra = 1


@admin.register(Metaverse)
class MetaverseAdmin(admin.ModelAdmin):
    inlines = [
        MetaverseVersionInline
    ]


class MetaverseInline(admin.StackedInline):
    model = Metaverse
    extra = 1


@admin.register(Multiverse)
class MultiverseAdmin(admin.ModelAdmin):
    inlines = [
        MetaverseInline
    ]
