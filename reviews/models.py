from enum import unique
from django.db import models

from users.models import TimeStampedModel, User

class Review(TimeStampedModel):
    title   = models.CharField(max_length=30)
    content = models.CharField(max_length=150)
    image   = models.CharField(max_length=300)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'