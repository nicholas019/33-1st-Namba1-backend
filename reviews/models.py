from django.db import models

from users.models import TimeStampedModel, User

class Review(TimeStampedModel):
    review_title   = models.CharField(max_length=30)
    review_content = models.CharField(max_length=150)
    review_image   = models.CharField(max_length=100)
    user           = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'