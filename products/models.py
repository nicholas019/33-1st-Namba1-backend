from itertools import product
from django.db import models

from core.models import TimeStampedModel

class Product(TimeStampedModel): 
    name        = models.CharField(max_length=15)
    description = models.CharField(max_length=300)
    serving     = models.IntegerField()
    cook_time   = models.IntegerField()
    prep_time   = models.IntegerField()
    price       = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        db_table = 'products'

class Spice(models.Model):
    spice   = models.CharField(max_length=15)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'spices'

class ProductImage(models.Model):
    image   = models.CharField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_images'

class Theme(models.Model):
    theme = models.CharField(max_length=15)

    class Meta:
        db_table = 'themes'

class ProductTheme(models.Model):
    theme   = models.ForeignKey(Theme, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_themes'