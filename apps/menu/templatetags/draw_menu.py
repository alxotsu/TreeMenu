from django import template
from django.core.exceptions import ObjectDoesNotExist

from apps.menu.actions import get_menu_hierarchy
from apps.menu.models import MenuItem

register = template.Library()


@register.inclusion_tag("menu/menu_template.html")
def draw_menu(menu_name, active_item_name=None):
    menu_items = MenuItem.objects.select_related('parent', 'menu').filter(menu__name=menu_name)
    if not menu_items.exists():
        raise ObjectDoesNotExist(f"The Menu \"{menu_name}\" does not exist or not contain items")
    hierarchy = get_menu_hierarchy(menu_items, active_item_name)
    s_hierarchy = str(hierarchy).replace("'", '"')
    return {
        "hierarchy": s_hierarchy,
        "menu_name": menu_name,
        "active_item_name": active_item_name,
        "menu_url": menu_items[0].menu.get_url()
    }
