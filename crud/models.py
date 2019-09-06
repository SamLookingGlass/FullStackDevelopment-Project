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
    description = models.CharField(max_length=255, null=True)
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
    item = models.ForeignKey('Item', on_delete=models.CASCADE) 
    stock = models.FloatField(null=True)
    def __str__(self):
        return self.item.name + " " 


