from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Berita(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now=True)
    writer = models.CharField(max_length=200,null=True)
    source = models.CharField(max_length=200,null=True)
