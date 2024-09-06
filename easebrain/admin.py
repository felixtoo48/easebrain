from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'updated_at')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'name', 'user_id', 'is_staff', 'created_at', 'updated_at')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_email', 'get_name', 'title', 'gender', 'phoneNumber', 'userLogo', 'addressLine1', 'birthDate', 'next_of_kin', 'maritalStatus', 'date_of_enrollment', 'summary', 'created_at', 'updated_at')

    def get_email(self, obj):
        return obj.user.email  # Access the email from the related User model

    def get_name(self, obj):
        return obj.user.name  # Access the name from the related User model

    get_email.short_description = 'Email'
    get_name.short_description = 'Name'

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(User, UserAdmin)

"""
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'title', 'phoneNumber', 'userLogo', 'addressLine1', 'postalCode')
"""
