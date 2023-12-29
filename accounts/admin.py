from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Experience
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['username','first_name', 'last_name', 'email', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('avatar', 'first_name', 'last_name', 'description','email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_verified', 'is_owner', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    readonly_fields = ['last_login', 'date_joined']


admin.site.register(Experience)
