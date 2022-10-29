from django.db import models

# Create your models here.
class Currency(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    icon = models.FilePathField(max_length=200)

class Exchange(models.Model):
    source_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="source_currency")
    target_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="target_currency")
    amount = models.DecimalField(max_digits=1000, decimal_places=6, null=True)
    change_1d = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    change_1w = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    change_1m = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    change_1y = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    change_1d_color = models.CharField(max_length=10, null=True)
    change_1w_color = models.CharField(max_length=10, null=True)
    change_1m_color = models.CharField(max_length=10, null=True)
    change_1y_color = models.CharField(max_length=10, null=True)
    last_updated = models.DateField(null=True)
