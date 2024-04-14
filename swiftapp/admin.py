from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import SwiftUser, UserItems

# Register your models here.
class SwiftUserAdmin(UserAdmin):
    list_display = ('email', 'last_name',  'first_name', 'avatar', 'date_joined', 'last_login','is_admin', 'is_active')
    search_field = ('email', 'last_name')#search_field

    fieldsets = ()
    '''(None, {'fields': ('email', 'password')}),  # Login credentials
    ('Personal Info', {'fields': ('first_name', 'last_name', 'phone', 'avatar')}),  # Personal details
    ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),  # User access control
    ('Important Dates', {'fields': ('last_login', 'date_joined')}),''' # System-generated timestamps


    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('email','first_name', 'last_name', 'phone', 'password1','password2','avatar')
        }),
    )
    ordering = ('email',)

admin.site.register(SwiftUser, SwiftUserAdmin)
admin.site.register(UserItems)