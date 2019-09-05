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
    price = models.FloatField(max_length=30, null=True)
    inventory = models.FloatField(max_length=30, null=True)
    size = models.ForeignKey('Size', on_delete=models.CASCADE, null=True)
    # Linked in admin.py
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # Linked in admin.py
    tags = models.ManyToManyField("Tag")
    product_image = models.ImageField(upload_to='images/', null=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, default='P')
    
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
    models.CharField(max_length=1, blank=False)
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

