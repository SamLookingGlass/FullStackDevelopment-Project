# Store carts item in sessions when user are logged in
from django.shortcuts import get_object_or_404
from crud.models import Item

def cart_contents(request):
    # Allow anything added to cart to be displayed on the webpage
    
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Item, pk=id)
        