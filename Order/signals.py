from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Product


@receiver(post_save, sender=Order)
def reduce_prod_qty(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        if product.quantity >= instance.quantity:
            product.quantity -= instance.quantity
            product.save()
        else:
            raise ValueError("Out of stock")