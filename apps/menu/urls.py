from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu_list_view, name="all_menu"),
    path('<str:menu_name>/<str:active_item_name>/', views.menu_view, name='menu_view_with_item'),
    path('<str:menu_name>/', views.menu_view, name='menu_view'),
]
