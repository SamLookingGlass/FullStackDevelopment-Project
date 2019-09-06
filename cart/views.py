from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    return render(request, 'checkout-page.html')
    
def add_to_cart(request, id):
    quantity = float(request.POST.get('quantity'))   
    
    cart = request.session.get('cart',{})
    cart[id] = cart.get(id, quantity)
    request.session['cart'] = cart
    return redirect(('item_list'))
    
def adjust_cart(request, id):
    quantity = float(request.POST.get('quantity'))   
    
    cart = request.session.get('cart',{})
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
