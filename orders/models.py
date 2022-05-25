from enum import unique
from django.db import models

from users.models import TimeStampedModel, User
from products.models import Product


class Cart(TimeStampedModel):
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    class Meta:
        unique_together = ('user', 'product')
        db_table = 'carts'

class OrderStatus(models.Model):
    status = models.CharField(max_length=15)

    class Meta:
        db_table = 'order_statuses'

class Order(TimeStampedModel):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=50)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'

class Invoice(models.Model):
    invoice = models.CharField(max_length=50)
    company = models.CharField(max_length=15)

    class Meta:
        db_table = 'invoices'

class OrderItem(models.Model): 
    order    = models.ForeignKey(Order, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    invoice  = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'order_items'