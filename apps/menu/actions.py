from django.db.models.query import QuerySet
from .models import MenuItem


def get_menu_hierarchy(menu_items: QuerySet[MenuItem], active_item_name: str or None = None) -> list[dict]:
    if len(menu_items) == 0:
        return list()

    items = dict()
    active_item = None
    for menu_item in menu_items:
        item = {
            'name': menu_item.name,
            'children': list(),
            'level': 0,
            'is_root': menu_item.parent_id is None,
        }
        items[item['name']] = item
        if item['name'] == active_item_name:
            active_item = item

    for menu_item in menu_items:
        item = items[menu_item.name]
        if not item['is_root']:
            parent = items[menu_item.parent.name]
            parent['children'].append(item)

    def set_levels(item):
        for child in item['children']:
            child['level'] = item['level'] + 1
            set_levels(child)

    result = list()
    for item in items.values():
        if item['is_root']:
            set_levels(item)
            result.append(item)

    if active_item is not None:
        for item in items.values():
            if item['level'] == active_item['level'] + 1:
                item['children'].clear()

    return result


def add_menu(menu_name, hierarchy: list[dict]) -> None:
    def add_item(item: dict, parent_object: MenuItem or None = None) -> MenuItem:
        menu_item = MenuItem(name=item['name'], menu_name=menu_name, parent=parent_object)
        menu_item.save()
        for child in item['children']:
            add_item(child, menu_item)
        return menu_item
    for root_item in hierarchy:
        add_item(root_item)

