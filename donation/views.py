from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib import messages
from donation.models import Donation
from dompet.models import Dompet
from dompet.models import ArusKas
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url="homepage:login")
def index(request):
    return render(request, 'donation.html')

@csrf_exempt
def add_donasi(request):
    if request.method == 'POST':
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

@csrf_exempt
def add_flutter(request):
    if request.method == 'POST':
        Donation(user=request.POST.get('user'), title=request.POST.get('title'), description=request.POST.get('description'), target=request.POST.get('target'), achieved=0, is_ongoing=True).save()
        return JsonResponse({'message': 'success'})
    return

@login_required(login_url="homepage:login")
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

@login_required(login_url="homepage:login")
def donasi_saya(request):
    if request.user.is_superuser:
        data = Donation.objects.all()
    else :
        data = Donation.objects.filter(user=request.user)
    context = {
        'donasi_saya': data
    }
    return render(request, 'donasi_saya.html', context)

@login_required(login_url="homepage:login")  
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
