from django.shortcuts import render
from .forms import ItemForm
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item

# Create your views here.
def show_todos(request):
    results = Item.objects.all()
    context = {
        "items" : results
    }
    return render(request, 'todo.html', context)
    
def create_item(request):
  if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(show_todos)
  else:
     form = ItemForm()
     return render(request, "create_items.html", {'form': form})

def edit_item(request, id):
    item = get_object_or_404(Item, pk=id)

    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(show_todos)
    else:
        form = ItemForm(instance=item)
    return render(request, "create_items.html", {'form': form})
    
def item_list(request):
    context = {
        'items' : Item.objects.all()
    }
    return render(request, "home-page.html", context)