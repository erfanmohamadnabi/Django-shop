from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type','profile_picture')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type','profile_picture')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)