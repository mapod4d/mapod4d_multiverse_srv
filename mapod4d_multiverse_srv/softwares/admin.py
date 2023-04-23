from django.contrib import admin

from .models import Software

# Register your models here.

#admin.site.register(Software)

@admin.register(Software)
class SoftwareAdmin(admin.ModelAdmin):
    readonly_fields = ["sversion"]
    ordering = [ 'name', '-v1', '-v2', '-v3', '-v4', 'so']

    @admin.display(description="SVersion")
    def sversion(self, obj):
        return obj.sversion

