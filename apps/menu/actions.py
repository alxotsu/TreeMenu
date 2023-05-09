from django.db.models.query import QuerySet
from .models import MenuItem


def get_menu_hierarchy(menu_items: QuerySet[MenuItem], active_item_name: str or None = None) -> list[dict]:
    if len(menu_items) == 0:
        return list()

    items = dict()
    root_items = list()
    active_item = None
    for menu_item in menu_items:
        item = {
            'name': menu_item.name,
            'children': list(),
            'level': 0,
        }
        items[item['name']] = item
        if menu_item.parent_id is None:
            root_items.append(item)
        if item['name'] == active_item_name:
            active_item = item

    for menu_item in menu_items:
        item = items[menu_item.name]
        if menu_item.parent_id is not None:
            parent = items[menu_item.parent.name]
            parent['children'].append(item)

    def set_levels(item):
        for child in item['children']:
            child['level'] = item['level'] + 1
            set_levels(child)

    for item in root_items:
        set_levels(item)

    if active_item is not None:
        def clear_item_children(item):
            if item['level'] > active_item['level']:
                item['children'].clear()
            else:
                for child in item['children']:
                    clear_item_children(child)

        for item in root_items:
            clear_item_children(item)

    return root_items


def add_menu(menu_name: str, hierarchy: list[dict]) -> list[MenuItem]:
    def add_item(item: dict, parent_object: MenuItem or None = None) -> MenuItem:
        menu_item = MenuItem(name=item['name'], menu_name=menu_name, parent=parent_object)
        menu_item.save()
        for child in item['children']:
            add_item(child, menu_item)
        return menu_item

    roots = list()
    for root_item in hierarchy:
        roots.append(add_item(root_item))
    return roots
