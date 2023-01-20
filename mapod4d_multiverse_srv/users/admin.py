from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import TabularInline
from .models import CustomUser
from projects.models import Project
#from .forms import CustomUserRegistrationForm, CustomUserChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Register your models here.

class ProjectInline(TabularInline):
    model = Project.users.through
    fields = ("id", "project")
    verbose_name = "Project"
    verbose_name_plural = "Projects"
    can_delete = False
    extra = 1

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser
    inlines = [ProjectInline]
    search_fields = ("email", )
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    ## list
    list_display = ('email', )
    ## view, chage fields
    fieldsets = (
        (None, {'fields': ('email', 'password', )}, ),
        (("Permissions"),
            {"fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
                ),
            },
        ),
    )
    ## create fields
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2', )}, ),
    )
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)


