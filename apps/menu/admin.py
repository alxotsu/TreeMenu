from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_name', 'parent', 'children')
    list_filter = ('menu_name', 'parent')
    search_fields = ('name',)
    ordering = ('menu_name', 'parent__name', 'name')

    def children(self, obj):
        return ', '.join([child.name for child in obj.children.all()])
