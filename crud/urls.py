from django.contrib import admin
from django.urls import path, include
from crud.views import show_todos, create_item, edit_item, item_list, HomeView, ItemDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/', show_todos, name='show_todos'),
    path('crud/create', create_item),
    path('crud/edit/<id>', edit_item),
    path('home/', HomeView.as_view(), name='item_list'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product')
]