from django.contrib import admin
from django.urls import path, include
# from crud.views import show_todos, create_item, edit_item, item_list, HomeView, ItemDetailView
from crud.views import item_list, product

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('crud/', show_todos, name='show_todos'),
    # path('crud/create', create_item),
    # path('crud/edit/<id>', edit_item),
    path('home/', item_list, name='item_list'),
    path('product/<id>', product, name='product')
]