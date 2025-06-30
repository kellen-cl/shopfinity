
from django.urls import path
from . import views  # make sure this import is working correctly

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('products/', views.product_list, name='product_list'),
    path('cart/', views.view_cart, name='cart_list'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('edit-cart-item/<int:product_id>/', views.edit_cart_item, name='edit_cart_item'),
    path('', views.product_list, name='products'),
    #path('create/', views.create_product, name='create_product'),
    #path('detail/<int:product_id>/', views.product_detail, name='product_detail'),
    #path('update/<int:product_id>/', views.update_product, name='update_product'),
    #path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]