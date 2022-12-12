from django.db import models
from django.contrib.auth.models import User


class Dompet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saldo = models.IntegerField()


class ArusKas(models.Model):
    dompet = models.ForeignKey(Dompet, on_delete=models.CASCADE)
    nominal = models.IntegerField()
    keterangan = models.CharField(max_length=255)
    tipe = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
