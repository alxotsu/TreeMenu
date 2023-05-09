from json import loads

from django.shortcuts import render

from .models import MenuItem
from .actions import get_menu_hierarchy, add_menu


def menu_list_view(request):
    names = list()
    for menu_item in MenuItem.objects.values("menu_name").distinct():
        names.append(menu_item['menu_name'])

    return render(request, "menu/menu_list.html", context={"menu_names": names})


def menu_view(request, menu_name, active_item_name=None):
    # Более удобный способ добавления меню по сравнению с админкой
    if request.method.lower() == "post":
        hierarchy = loads(request.body)
        add_menu(menu_name, hierarchy)

    menu_items = MenuItem.objects.select_related('parent').filter(menu_name=menu_name)
    hierarchy = get_menu_hierarchy(menu_items, active_item_name)

    s_hierarchy = str(hierarchy).replace("'", '"')
    return render(request, "menu/menu.html", context={
        "hierarchy": s_hierarchy,
        "menu_name": menu_name,
        "active_item_name": active_item_name,
    })
