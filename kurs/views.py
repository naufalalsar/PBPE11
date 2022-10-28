from django.shortcuts import render
from kurs.models import Currency

# Create your views here.
def kurs(request):
    currencies = Currency.objects.all()
    context = {"currencies": currencies}
    return render(request, 'kurs.html', context)
