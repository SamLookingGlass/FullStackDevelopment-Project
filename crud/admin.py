from django.contrib import admin
from .models import Item, Category , Tag, OrderItem, Order

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(OrderItem)
admin.site.register(Order)
# Register your models here.
