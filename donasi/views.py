from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.core import serializers
from donasi.forms import DonasiForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from donasi.models import Donasi


@login_required(login_url="homepage:login")
# Create your views here.
def index(request):
    # form = DonasiForm()
    # if request == 'POST':
    #     form = DonasiForm(request.POST)
    #     if form.is_valid():
    #         new_form = form.save(commit=False)
    #         new_form.user = request.user
    #         new_form.achieved = 0
    #         new_form.save()
    #         return redirect('donasi:index')

    # context = {'form': form}
    return render(request, 'donasi.html')


@login_required(login_url="homepage:login")
def add_donasi(request):
    if request.method == 'POST':
        
        # user = request.user
        # title = request.POST.get("harga_barang")
        # deskripsi = request.POST.get("deskripsi")

        new_task = Donasi(user=request.user, 
                    title=request.POST.get('title'), 
                    description=request.POST.get('description'),
                    target=request.POST.get('target'),
                    achieved=0
                    )
        new_task.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@login_required(login_url="homepage:login")
def transaksi_donasi(request, id):
    # data = Donasi.objects.filter(pk=id)
    # // Jika JSON
    # return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    context = {}
    return render(request, 'transaksi_donasi.html', context)

@login_required(login_url="homepage:login")
def show_json(request):
    item = Donasi.objects.all()
    return HttpResponse(serializers.serialize('json', item))