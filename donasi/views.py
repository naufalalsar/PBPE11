
from donasi.forms import DonasiForm
from django.shortcuts import render, redirect

from donasi.models import Donasi

# Create your views here.
def index(request):
    return render(request, 'donasi.html')

def add_donasi(request):
    form = DonasiForm()
    if request == 'POST':
        form = DonasiForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('donasi:index')

    context = {'form': form}
    return render(request, 'add_donasi.html', context)
