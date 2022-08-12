from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'password', 'role', 'date_created', 'date_updated', 'is_superuser']


admin.site.register(User, MyUserAdmin)