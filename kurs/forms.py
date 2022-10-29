from django.forms import ModelForm
from kurs.models import Currency, Exchange

class ExchangeForm(ModelForm):
    class Meta:
        model = Exchange
        fields = ['source_currency', 'target_currency', 'amount', 'last_updated']