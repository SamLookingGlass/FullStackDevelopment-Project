from django import forms
from .models import Item
from pyuploadcare.dj.forms import ImageField

class ItemForm(forms.ModelForm):
    product_image = ImageField(label='Photo')
    class Meta:
        model = Item
        fields = ('name', 'category', 'product_image')
        
        