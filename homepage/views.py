from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from dompet.models import Dompet
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("homepage:homepage"))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {"button_hidden": True}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('homepage:login'))
    return response

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            new_user = User.objects.get(username=form.cleaned_data.get('username'))
            Dompet.objects.create(user=new_user, saldo=0).save()

            return redirect('homepage:login')
    
    context = {"button_hidden": True}
    return render(request, 'register.html', context)
