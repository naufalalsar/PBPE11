from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from berita.models import Berita
from django.http import JsonResponse
from berita.forms import BeritaForm

# Create your views here.

def show(request):
    if request.user.is_superuser:
        try:
            count = request.COOKIES['news_count']
        except:
            response = HttpResponseRedirect(reverse("berita:show"))
            response.set_cookie('news_count', 0)
            return response
        form = BeritaForm(request.user)
        try :
            context = {
                'last_news' : request.session['last_news'],
                'count' : count,
                'form' : form,
            }
        except :
            context = {
                'last_news' : 'No Last Seen News Yet',
                'count' : count,
                'form' : form,
            }
        if request.method == 'POST':
            form = BeritaForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'success'})
        return render(request, "admin.html", context)
    else:
        try:
            count = request.COOKIES['news_count']
        except:
            response = HttpResponseRedirect(reverse("berita:show"))
            response.set_cookie('news_count', 0)
            return response
        try :
            context = {
            'last_news' : request.session['last_news'],
            'count' : count,
            }
        except :
            context = {
            'last_news' : 'No Last Seen News Yet',
            'count' : count,
            }
        return render(request, "user.html", context)

def json_all(request):
    data = Berita.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url="homepage:login")
def delete(request, pk):
    if request.user.is_superuser:
        Berita.objects.filter(pk=pk).delete()
        return JsonResponse({'message': 'success'})
    else:
        return render(request, "forbidden.html")   

@login_required(login_url="homepage:login")
def add(request):
    if request.user.is_superuser:
        form = BeritaForm()
        if request.method == 'POST':
            form = BeritaForm(request.POST, user=request.user)
            return JsonResponse({'message': 'success'})
        context = {
            'form' : form,
        }
        return render(request, "create.html", context)
    else:
        return render(request, "forbidden.html")


def berita(request, pk):
    data = Berita.objects.filter(pk=pk)
    request.session['last_news'] = data[0].title
    context = {
        'data' : data,
        'pk' : pk,
    }
    response = render(request, "berita.html", context)
    response.set_cookie('news_count', int(request.COOKIES['news_count'])+1)
    return response

@login_required(login_url="homepage:login")
def delete_filter(request, pk):
    if request.user.is_superuser:
        Berita.objects.filter(pk=pk).delete()
        return redirect('berita:show')
    else:
        return render(request, "forbidden.html")




