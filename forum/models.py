from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Forum(models.Model):
    judul = models.CharField(max_length=200, null=True)
    isi = models.TextField(blank=True, null=True)
    tanggal = models.DateTimeField(auto_now=True)
    komenPertama = models.TextField(default="Belum ada komentar")

class Komen(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, null=True)
    komen = models.TextField(null=True, blank=True)
    tanggal = models.DateTimeField(auto_now=True)
    idforum = models.BigIntegerField(null=True)
