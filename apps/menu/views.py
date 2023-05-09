from json import loads

from django.shortcuts import render

from .models import Menu
from .actions import add_menu


def menu_list_view(request):
    return render(request, "menu/menu_list.html", context={"menu_list": Menu.objects.all()})


def menu_view(request, menu_name, active_item_name=None):
    # Более удобный способ добавления меню по сравнению с админкой
    if request.method.lower() == "post":
        hierarchy = loads(request.body)
        add_menu(menu_name, hierarchy)

    return render(request, "menu/menu.html", context={
        "menu_name": menu_name,
        "active_item_name": active_item_name,
    })
