from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
#from .forms import CustomUserRegistrationForm, CustomUserChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Register your models here.

#class CustomUserAdmin(UserAdmin):
#    add_form = CustomUserRegistrationForm
#    form = CustomUserChangeForm
#    #model = CustomUser
#
#    ordering = ('email',)
#    list_display = ('email', )
#    fieldsets = (
#        (None,
#            {'fields': ('email', 'password', )}),
#        (("Permissions"),
#            {
#                "fields": (
#                    "is_active",
#                    "is_staff",
#                    "is_superuser",
#                    "groups",
#                    "user_permissions",
#                ),
#            },
#        ),
#        (("Important dates"), {"fields": ("last_login", "date_joined")}),
#    )
#    add_fieldsets = (
#        (None, {'fields': ('email', 'password', 'password2')}),
#    )



#class CustomUserAdmin(admin.ModelAdmin):
#    exclude = ('password',)
#    ordering = ('email',)
#    list_display = ('email', 'is_superuser',)
#    search_fields = ('email',)
#    list_filter = ('is_superuser',)
#    readonly_fields = ('email',)

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    search_fields = ("email", )
    ## list
    list_display = ('email', )
    ## view, chage fields
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
    )
    ## create fields
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2', )}),
    )
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)


