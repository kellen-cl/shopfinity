from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Order(models.Model):
   # user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)#retrieves the products for you from the products app
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,default='Pending')

def __str__(self):
        return f"Order #{self.id} - {self.product.name}"
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)# if an order is deleted, delete the order
    product = models.ForeignKey(Product, on_delete=models.CASCADE)# if a product is deleted, delete the order
    quantity = models.IntegerField()

    def __str__(self): #converts to string
        return f"{self.order.id} - {self.quantity}pcs - {self.product.name}"
    
