from django.urls import path
from . import views#import all views from the current directory

urlpatterns = [
    path('', views.order_list, name='order_list'),#List all orders
    path('complete-order/', views.complete_order, name='complete_order'),
    path('orders/cancel/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('orders/', views.orders_view, name='orders'),
     path('contact/', views.contact_view, name='contact'),
   # path('create/', views.create_order, name='create_order'),
   # path('detail/<int:order_id>/', views.order_detail, name='order_detail'),#detail of an order
    #path('update/<int:order_id>/', views.update_order, name='update_order'),#edit an order
   # path('delete/<int:order_id>/', views.delete_order, name='delete_order'),#delete an order

    path('checkout/', views.checkout, name='checkout'),
    path('my-orders/', views.my_orders, name='my_orders')
]