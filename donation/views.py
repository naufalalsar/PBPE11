from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import render, redirect

from donation.models import Donation

# Create your views here.
def index(request):
    return render(request, 'donation.html')

def add_donasi(request):
    if request.method == 'POST':
        
        # user = request.user
        # title = request.POST.get("harga_barang")
        # deskripsi = request.POST.get("deskripsi")

        new_task = Donation(user=request.user, 
                    title=request.POST.get('title'), 
                    description=request.POST.get('description'),
                    target=request.POST.get('target'),
                    achieved=0,
                    is_ongoing=True
                    )
        new_task.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def transaksi_donasi(request, id):
    data = Donation.objects.get(pk=id)
    if request.method == 'POST':
        data.achieved += int(request.POST.get('jumlahDonasi'))
        data.save()
    data = Donation.objects.filter(pk=id)
    context = {
        'donasi': data
    }

    return render(request, 'transaksi_donation.html', context)

def show_json(request):
    item = Donation.objects.all()
    return HttpResponse(serializers.serialize('json', item))