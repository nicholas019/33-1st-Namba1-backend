from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True


class User(TimeStampedModel):
    email        = models.CharField(max_length=45)
    name         = models.CharField(max_length=15)
    password     = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    brithday     = models.DateField()
    address      = models.CharField(max_length=45)
    agreement    = models.JSONField()

    class Meta:
        db_table = 'users'

class Delivery(models.Model):
    take_name        = models.CharField(max_length=15)
    take_phonenumber = models.CharField(max_length=15)
    take_homenumber  = models.CharField(max_length=15)
    address          = models.CharField(max_length=15)
    user             = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'deliveries'
