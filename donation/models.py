from django.db import models
from django.contrib.auth.models import User

class Donation(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    target = models.IntegerField()
    achieved = models.IntegerField()
    is_ongoing = models.BooleanField()

