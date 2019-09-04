from django.db import models
from django.conf import settings

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    price = models.FloatField(null=True)
    # Linked in admin.py
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # Linked in admin.py
    tags = models.ManyToManyField("Tag")
    product_image = models.ImageField(upload_to='images/', null=True)
    def __str__(self):
        return self.name
        
class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)
    def __str__(self):
        return self.name
        
class Tag(models.Model):
    name = models.CharField(max_length=50, blank=False)
    def __str__(self):
        return self.name        

# Link between 2 models
class OrderItem(models.Model):
    def __str__(self):
        return self.name        

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return self.name        

