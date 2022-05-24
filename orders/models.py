from django.db import models

from users.models import TimeStampedModel, User


class OrderStatus(models.Model):
    status = models.CharField(max_length=15)

    class Meta:
        db_table = 'orderstatus'

class Order(TimeStampedModel):
    user     = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    order_number = models.CharField(max_length=50)
    order_status = models.ForeignKey(OrderStatus, related_name='order_status', on_delete=models.CASCADE)

    class Meta:
        db_table = 'order'




