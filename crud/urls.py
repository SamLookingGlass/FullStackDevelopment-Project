from django.contrib import admin
from django.urls import path, include
from crud.views import item_list, product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', item_list, name='item_list'),
    path('product/<id>', product, name='product')
]