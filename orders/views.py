from django.shortcuts import render
from django.shortcuts import render, redirect
from products.models import Product  # To get product info
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def create_order(request):
    return render(request, 'orders/create_order.html')#Logic to create an order

def order_detail(request, order_id):
    return render(request, 'orders/order_detail.html', {'order_id': order_id})#logic to view order details

def edit_order(request, order_id):
    return render(request, 'orders/edit_order.html', {'order_id': order_id})#logic to edit an order

def delete_order(request, order_id):
    return render(request, 'orders/delete_order.html', {'order_id': order_id})#logic to delete an order

def complete_order(request):
    return render(request, 'orders/complete_order.html')
    return HttpResponse("Order completed!")







@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('view_cart')

    order = Order.objects.create(user=request.user)

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity
        )

    # Clear cart after checkout
    request.session['cart'] = {}
    return render(request, 'orders/checkout_success.html', {'order': order})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})

def order_list(request):
    orders = Order.objects.select_related('product').all()  # load orders with items
    return render(request, 'orders/order_list.html', {'orders': orders})

def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()  # or set status = "cancelled" if you have a status field
    return redirect('order_list')  # redirect back to the list after cancel

def orders_view(request):
    return render(request, 'orders.html')


def contact_view(request):
    return render(request, 'contact.html')