from django.contrib import admin

from .models import Software

# Register your models here.

#admin.site.register(Software)

@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    readonly_fields = ["sversion"]

    @admin.display(description="SVersion")
    def sversion(self, obj):
        return obj.sversion

