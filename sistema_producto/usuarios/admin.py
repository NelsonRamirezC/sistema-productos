from django.contrib import admin
from django.contrib.auth.models import Permission
# Register your models here.

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'codename', 'content_type')
    search_fields = ('name', 'codename')
