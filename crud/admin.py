from django.contrib import admin
from .models import Item, Category , Tag, OrderItem, Order, Size, Inventory

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Size)
admin.site.register(Inventory)

# Register your models here.
