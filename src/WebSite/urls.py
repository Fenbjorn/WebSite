from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from .views import index, pages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('<str:other_pages>/', pages, name='pages'),
]

urlpatterns += staticfiles_urlpatterns()
