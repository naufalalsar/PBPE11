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
from forum.models import Forum, Komen
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# @login_required(login_url="homepage:login")
def show_forum(request):
        return render(request, "forum_user.html")


def show_komen(request, pk):
    if(request.user.is_superuser):
        data = Forum.objects.filter(pk=pk)
        context = {
        'data' : data,
        'pk' : pk,
        }
        return render(request, "forumkomen_admin.html", context)
    elif(request.user.is_authenticated):
        data = Forum.objects.filter(pk=pk)
        context = {
        'data' : data,
        'pk' : pk,
        }
        return render(request, "forumkomen_user.html", context)
    else:
        return render(request, "not_login.html")


def json_forum_all(request):
        data = Forum.objects.all()
        for forum in data :
            komen = Komen.objects.filter(forum = forum)
            if komen:
                forum.komenPertama = komen[0].komen
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")



def json_komen(request, pk):
        data = Komen.objects.filter(forum=Forum.objects.get(id=pk))
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def add_forum(request):
        if request.method == 'POST':
            Forum(user=request.user, judul=request.POST.get('judul'), isi=request.POST.get('isi')).save()
            return JsonResponse({'message': 'success'})
            
@login_required(login_url="homepage:login")
@csrf_exempt
def create_forum(request):
    context = {}
    if request.method == "POST":
        temp = Forum(judul=request.POST.get('judul'),isi=request.POST.get('isi'))
        temp.save()
        return JsonResponse({'message': 'success'})
    return render(request, "create_forum.html")


def add_komen(request, pk):
        if request.method == 'POST':
            Komen(forum=Forum.objects.get(id=pk),komen=request.POST.get('komen'),user=request.user,idforum=request.POST.get('idforum')).save()
            return JsonResponse({'message': 'success'})

@login_required(login_url="homepage:login")
@csrf_exempt
def delete_forum(request, pk):
        Forum.objects.filter(pk=pk).delete()
        return JsonResponse({'message': 'success'})



def delete_komen(request,pk):
        Komen.objects.filter(pk=pk).delete()
        return JsonResponse({'message': 'success'})


def json_komen_user(request):
        data = Komen.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def json_forum_user(request):
        data = Forum.objects.filter(user=request.user)
        for forum in data :
            komen = Komen.objects.filter(forum = forum)
            if komen:
                forum.komenPertama = komen[0].komen
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def delete_forum_user(request):
        return render(request, "delete_forum_user.html")



def delete_komen_user(request):
        return render(request, "delete_komen_user.html")








