from django.contrib import admin
from.models import Order
from. models import OrderItem

# Register your models here.

admin.site.register(Order)
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')
