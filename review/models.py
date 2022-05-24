from django.db import models

from users.models import TimeStampedModel, User

class Review(TimeStampedModel):
    review_content = models.TextField()
    review_image   = models.CharField(max_length=100)
    user           = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'



