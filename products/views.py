from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart
from django.contrib import messages

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def view_cart(request):
    cart_items = Cart.objects.all()  # Optional: filter by user later
    total_price = sum(item.total_price for item in cart_items)

    return render(request, 'products/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


def cart_list(request):
    cart_items = Cart.objects.all()  # Later: filter by user/session
    total_price = sum(item.total_price for item in cart_items)

    return render(request, 'products/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def add_to_cart(request, product_id):
    try:
        quantity = int(request.POST.get('quantity', 1))
    except ValueError:
        quantity = 1

    product = get_object_or_404(Product, id=product_id)

    # ✅ Provide total_price and quantity when creating new cart item
    cart_item, created = Cart.objects.get_or_create(
        product=product,
        defaults={
            'quantity': quantity,
            'total_price': product.price * quantity
        }
    )

    if not created:
        # Update quantity and price if already exists
        cart_item.quantity += quantity
        cart_item.total_price = product.price * cart_item.quantity
        cart_item.save()
        messages.success(request, f'Quantity for {cart_item.product.name} updated to {cart_item.quantity}.')
    else:
        # Already created correctly with total_price from defaults
        messages.success(request, f'{cart_item.product.name} added to cart.')

    return redirect('cart_list')

    # This part below will never run because of the return statement above.
    # If you want to use session-based cart, comment out the model-based logic above and use the code below instead.

    # product_id_str = str(product_id)
    # if product_id_str in cart:
    #     cart[product_id_str] += quantity
    # else:
    #     cart[product_id_str] = quantity
    #
    # request.session['cart'] = cart
    # return redirect('cart_list')

def remove_from_cart(request, product_id):
    try:
        cart_item = Cart.objects.get(product_id=product_id)
        cart_item.delete()
        messages.success(request, 'Item removed from cart.')
    except Cart.DoesNotExist:
        messages.error(request, 'Item not found in cart.')
    return redirect('cart_list')  # or 'cart_list' depending on naming

def edit_cart_item(request, product_id):
    cart_item=get_object_or_404(Cart, product_id=product_id)
    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity', 1))  # Get the quantity from the form
            if quantity <1:
                quantity=1
        except ValueError:
                quantity=1

        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, f'Quantity for {cart_item.product.name} updated to {cart_item.quantity}.')
        return redirect('cart_list')
    
    return render(request, 'products/edit_cart_item.html', {'cart_item': cart_item})
   
