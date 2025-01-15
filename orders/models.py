from django.db import models
from products.models import Product

# Create your models here.

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Calculate the Total Price Before Saving the Order
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"