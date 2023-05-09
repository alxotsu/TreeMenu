from json import loads

from django.http.response import HttpResponse
from django.shortcuts import render

from .models import MenuItem
from .actions import get_menu_hierarchy, add_menu


def menu_list_view(request):
    names = list()
    for menu_item in MenuItem.objects.values("menu_name").distinct():
        names.append(menu_item['menu_name'])

    return HttpResponse(names, status=200, content_type="Application/json")


def menu_view(request, menu_name, active_item_name=None):
    # Более удобный способ добавления меню по сравнению с админкой
    if request.method.lower() == "post":
        hierarchy = loads(request.body)
        add_menu(menu_name, hierarchy)

    menu_items = MenuItem.objects.select_related('parent').filter(menu_name=menu_name).order_by('parent_id')
    hierarchy = get_menu_hierarchy(menu_items, active_item_name)

    return HttpResponse(hierarchy, status=200, content_type="Application/json")

