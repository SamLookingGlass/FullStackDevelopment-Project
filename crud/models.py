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
<<<<<<< HEAD
    price = models.FloatField(null=True)
    product_image = models.ImageField(upload_to='images/', null=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, default='P')
=======
    price = models.FloatField(max_length=30, null=True)
    inventory = models.FloatField(max_length=30, null=True)
    size = models.ForeignKey('Size', on_delete=models.CASCADE, null=True)
>>>>>>> ec0693cbd12b0fdf966884da7b4e23c413954e80
    # Linked in admin.py
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag")
<<<<<<< HEAD
    size = models.ForeignKey('Size', on_delete=models.CASCADE)
=======
    product_image = models.ImageField(upload_to='images/', null=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, default='P')
    
>>>>>>> ec0693cbd12b0fdf966884da7b4e23c413954e80
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
<<<<<<< HEAD
    name = models.CharField(max_length=30, blank=False)
    def __str__(self):
        return self.name

=======
    models.CharField(max_length=1, blank=False)
    def __str__(self):
        return self.name
    
    
>>>>>>> ec0693cbd12b0fdf966884da7b4e23c413954e80
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

