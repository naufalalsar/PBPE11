from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib import messages
from donation.models import Donation
from dompet.models import Dompet
from dompet.models import ArusKas

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
    try :
        dompet = Dompet.objects.get(user=request.user)
    except Dompet.DoesNotExist:
        dompet = Dompet.objects.create(user=request.user, saldo=0)
    if request.method == 'POST':
        if dompet.saldo < int(request.POST.get('jumlahDonasi')):
            messages.error(request, "Saldo kurang!")
            data = Donation.objects.filter(pk=id)
            context = {
                'donasi': data
            }
            return render(request, 'transaksi_donation.html', context)
        arus_kas = ArusKas.objects.create(
        dompet=dompet, nominal=int(request.POST.get('jumlahDonasi')), keterangan='Donasi '+data.title, tipe=-1
        )
        temp_saldo = dompet.saldo + -1*arus_kas.nominal
        dompet.saldo = temp_saldo
        dompet.save()
        data.achieved += int(request.POST.get('jumlahDonasi'))
        data.save()
    data = Donation.objects.filter(pk=id)
    context = {
        'donasi': data
    }

    return render(request, 'transaksi_donation.html', context)

def donasi_saya(request):
    data = Donation.objects.filter(user=request.user)
    context = {
        'donasi_saya': data
    }
    return render(request, 'donasi_saya.html', context)
    
def hapus_donasi(request, id):
    item = Donation.objects.filter(pk=id)
    item.delete()
    data = Donation.objects.filter(user=request.user)
    context = {
        'donasi_saya': data,
    }
    messages.info(request, 'Donasi berhasil terhapus!')
    return redirect('donation:donasi_saya')

def show_json(request):
    item = Donation.objects.all()
    return HttpResponse(serializers.serialize('json', item))