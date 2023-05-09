from django.contrib import admin
from .models import MenuItem, Menu


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'parent', 'children')
    list_filter = ('menu__name', 'parent')
    search_fields = ('name',)
    ordering = ('menu__name', 'parent__name', 'name')

    def children(self, obj):
        return ', '.join([child.name for child in obj.children.all()])


@admin.register(Menu)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name', 'urls')
    ordering = ('name',)
