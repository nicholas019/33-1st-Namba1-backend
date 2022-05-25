from django.db import models

from users.models import TimeStampedModel

class Product(TimeStampedModel):
    product_name    = models.CharField(max_length=15)
    product_content = models.CharField(max_length=300)
    people          = models.IntegerField()
    cook_time       = models.IntegerField()
    setting_time    = models.IntegerField()
    selling_price   = models.DecimalField(max_digits=9, decimal_places=2)
    discount_price  = models.DecimalField(max_digits=9, decimal_places=2, null=True)

    class Meta:
        db_table = 'products'

class ProductImage(models.Model):
    product_image = models.CharField(max_length=100)
    product       = models.ForeignKey(Product, on_delete=models.CASCADE)

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
        db_table = 'product_theme'