from django.db import models
from django.contrib.auth.models import User

class Donasi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField()

