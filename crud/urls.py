from django.contrib import admin
from django.urls import path, include
from crud.views import show_todos, create_item, edit_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/', show_todos, name='show_todos'),
    path('crud/create', create_item),
    path('crud/edit/<id>', edit_item),
]