from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('apps.menu.urls')),
    path("", RedirectView.as_view(url="menu/", permanent=False), name='index')
]
