from django.db import models


from users.models import TimeStampedModel, User
from products.models import Product

class Cart(TimeStampedModel):
    user     = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    class Meta:
        db_table = 'cart'

