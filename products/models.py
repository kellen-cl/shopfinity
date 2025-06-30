from django.db import models

# Product model
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Cart model (should NOT be indented under Product)
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#save methid to calculate the total price
#this method is called when the model instance is saved
def save(self, *args, **kwargs):
        #  Automatically calculate total_price before saving
        if self.product and self.quantity:
            self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

def __str__(self):
        return f"{self.quantity} x {self.product.name}"

def __str__(self):
        return f"{self.quantity} x {self.product.name}"
