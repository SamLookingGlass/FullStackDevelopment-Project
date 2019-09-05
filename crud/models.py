from django.db import models
from django.conf import settings

# Label Choices
LABEL_CHOICES = (
    ('P','primary'),
    ('S','secondary'),
    ('D','danger')
)


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    price = models.FloatField(null=True)
    product_image = models.ImageField(upload_to='images/', null=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, default='P')
    # Linked in admin.py
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag")
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

class Size(models.Model):
    name = models.CharField(max_length=30, blank=False)
    def __str__(self):
        return self.name

class Inventory(models.Model):
    name = models.ForeignKey('Item', on_delete=models.CASCADE) 
    size = models.ForeignKey('Size', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# Link between 2 models
class OrderItem(models.Model):
    item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)
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

