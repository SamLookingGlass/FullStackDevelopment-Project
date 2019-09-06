from django.shortcuts import render
from .forms import ItemForm
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item


# Diplay all products 
def item_list(request):
    results = Item.objects.all()
    context = {
        'items' : results
    }
    return render(request, "home-page.html", context)

# Display selected product 
def product(request, id):
    results = Item.objects.get(pk=id)
    context = {
        'items' : results
    }
    return render(request, "product-page.html", context)
    