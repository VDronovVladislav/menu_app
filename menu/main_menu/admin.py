from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin

from main_menu.models import MenuItem


class MenuItemAdmin(DjangoMpttAdmin):
    mptt_level_indent = 20


admin.site.register(MenuItem, MenuItemAdmin)
