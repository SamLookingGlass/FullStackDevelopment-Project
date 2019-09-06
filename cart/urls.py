from django.urls import path, include
from django.conf.urls import url
from cart.views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    path('cart/', view_cart, name='view_cart'),
    path('add/<id>', add_to_cart, name='add_to_cart'),
    path('adjust/<id>',adjust_cart, name='adjust_cart')
]