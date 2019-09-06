from django.contrib import admin
from .models import Item, Category, Tag, Size, Inventory

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Size)
admin.site.register(Inventory)

# Register your models here.
