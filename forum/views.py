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

# Create your views here.

@login_required(login_url="hompage:login")
def show_forum(request):
    if(request.user.is_superuser):
        return render(request, "forum_admin.html")
    elif(request.user.is_authenticated):
        return render(request, "forum_user.html")
    else:
        return render(request, "not_login.html")

@login_required(login_url="hompage:login")
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

@login_required(login_url="hompage:login")
def json_forum_all(request):
    if(request.user.is_authenticated):
        data = Forum.objects.all()
        for forum in data :
            komen = Komen.objects.filter(forum = forum)
            if komen:
                forum.komenPertama = komen[0].komen
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    else:
        return render(request, "not_login.html")

@login_required(login_url="hompage:login")
def json_komen(request, pk):
    if(request.user.is_authenticated):
        data = Komen.objects.filter(forum=Forum.objects.get(id=pk))
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    else:
        return render(request, "not_login.html")

@login_required(login_url="hompage:login")
def add_forum(request):
    if(request.user.is_authenticated):
        if request.method == 'POST':
            Forum(user=request.user, judul=request.POST.get('judul'), isi=request.POST.get('isi')).save()
            return JsonResponse({'message': 'success'})
    else :
        return render(request, "not_login.html")

@login_required(login_url='/homepage/login/')
def create_forum(request):
    context = {}
    if request.method == "POST":
        temp = Forum(user=request.user, judul=request.POST.get('judul'),isi=request.POST.get('isi'))
        temp.save()
        return redirect('forum:show_forum')
    return render(request, "create_forum.html",context)

@login_required(login_url="hompage:login")
def add_komen(request, pk):
    if(request.user.is_authenticated):
        if request.method == 'POST':
            Komen(forum=Forum.objects.get(id=pk),komen=request.POST.get('komen'),user=request.user,idforum=request.POST.get('idforum')).save()
            return JsonResponse({'message': 'success'})
    else :
        return render(request, "not_login.html")

@login_required(login_url="hompage:login")
def delete_forum(request, pk):
    if(request.user.is_authenticated):
        Forum.objects.filter(pk=pk).delete()
        return JsonResponse({'message': 'success'})
    else :
        return render(request, "not_login.html")

@login_required(login_url="hompage:login")
def delete_komen(request,pk):
    if(request.user.is_authenticated):
        Komen.objects.filter(pk=pk).delete()
        return JsonResponse({'message': 'success'})
    else :
        return render(request, "not_login.html")

@login_required(login_url="hompage:login")
def json_komen_user(request):
    if(request.user.is_authenticated):
        data = Komen.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    else :
        return render(request, "not_login.html")

@login_required(login_url="hompage:login")
def json_forum_user(request):
    if(request.user.is_authenticated):
        data = Forum.objects.filter(user=request.user)
        for forum in data :
            komen = Komen.objects.filter(forum = forum)
            if komen:
                forum.komenPertama = komen[0].komen
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    else :
        return render(request, "not_login.html")

@login_required(login_url="hompage:login")
def delete_forum_user(request):
    if(request.user.is_authenticated):
        return render(request, "delete_forum_user.html")
    else :
        return render(request, "not_login.html")

@login_required(login_url="hompage:login")
def delete_komen_user(request):
    if(request.user.is_authenticated):
        return render(request, "delete_komen_user.html")
    else :
        return render(request, "not_login.html")







