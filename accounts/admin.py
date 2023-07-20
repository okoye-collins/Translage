from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser, UserProfile
from django.contrib.auth.models import Group

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    list_display = ('email', 'username', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'is_superuser')

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if not request.user.is_superuser:
            # Remove 'groups' field from non-superuser fieldsets
            fieldsets = [
                (name, field_data)
                for name, field_data in fieldsets
                if 'groups' not in field_data['fields']
            ]
        return fieldsets

    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.unregister(Group)

