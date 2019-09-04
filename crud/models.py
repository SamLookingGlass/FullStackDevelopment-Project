from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
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