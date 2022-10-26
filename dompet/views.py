from django.shortcuts import render
from dompet.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import redirect

@login_required(login_url='homepage:login')
def show_dompet(request):
    dompet = Dompet.objects.get(user=request.user)
    context = {"dompet": dompet}
    return render(request, "dompet.html", context=context)

@login_required(login_url='homepage:login')
def show_arus_kas(request):
    arus_kas = ArusKas.objects.filter(dompet__user=request.user)
    context = {"arus_kas": arus_kas}
    return render(request, "arus_kas.html", context=context)

@login_required(login_url='homepage:login')
def create_arus_kas(request):
    if request.method == "POST":
        dompet = Dompet.objects.get(user=request.user)
        nominal = request.POST.get("nominal")
        keterangan = request.POST.get("keterangan")
        tipe = request.POST.get("tipe")
        ArusKas.objects.create(dompet=dompet, nominal=nominal, keterangan=keterangan, tipe=tipe).save()
        return redirect("dompet:show_dompet")

@login_required(login_url='homepage:login')
def create_arus_kas_ajax(request):
    if request.method == "POST":
        nominal = request.POST.get('nominal')
        keterangan = request.POST.get('keterangan')
        tipe = request.POST.get('tipe')
        dompet = Dompet.objects.get(user=request.user)
        dompet.saldo = dompet.saldo + tipe * nominal
        if dompet.saldo < 0:
            return JsonResponse({"status": "error", "message": "Saldo tidak boleh negatif!"})
        
        arus_kas = ArusKas.objects.create(dompet=dompet, nominal=nominal, keterangan=keterangan, tipe=tipe).save()
        dompet.save()
        return JsonResponse({
            "status": "success",
            "nominal": nominal,
            "keterangan": keterangan,
            "tipe": tipe,
            "created_at": arus_kas.created_at
        })

    return JsonResponse({"status": "error"})