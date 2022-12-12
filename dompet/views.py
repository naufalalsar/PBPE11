from django.shortcuts import render
from dompet.models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib import messages
from .forms import ArusKasForm
import datetime


def show_dompet(request, filter_type="all"):
    try:
        # dompet = Dompet.objects.get(user=request.user)
        dompet = Dompet.objects.all()[1]
    except (Dompet.DoesNotExist, IndexError) as e:
        dompet = Dompet.objects.create(saldo=0)

    # arus_kas = ArusKas.objects.filter(dompet=dompet)
    arus_kas = ArusKas.objects.all()
    if filter_type == "date":
        arus_kas = arus_kas.filter(created_at__date=datetime.date.today())
    elif filter_type == "week":
        arus_kas = arus_kas.filter(
            created_at__week=datetime.date.today().isocalendar()[1],
            created_at__year=datetime.date.today().isocalendar()[0],
            created_at__month__gte=datetime.date.today().month,
        )
    elif filter_type == "month":
        arus_kas = arus_kas.filter(created_at__month=datetime.date.today().month)
    elif filter_type == "year":
        arus_kas = arus_kas.filter(created_at__year=datetime.date.today().year)
    elif filter_type == "all":
        pass
    else:
        return JsonResponse({"status": "error"})

    pemasukan, pengeluaran = 0, 0
    for arus in arus_kas:
        if arus.tipe == 1:
            pemasukan += arus.nominal
        else:
            pengeluaran += arus.nominal
    total = pemasukan - pengeluaran
    is_positive = total >= 0
    total = abs(total)

    print(dompet)

    context = {
        "dompet": dompet,
        "pemasukan": pemasukan,
        "pengeluaran": pengeluaran,
        "total": total,
        "is_positive": is_positive,
    }
    return render(request, "dompet.html", context=context)


def show_dompet_json(request):
    try:
        # dompet = Dompet.objects.get(user=request.user)
        dompet = Dompet.objects.all()[1]
    except (Dompet.DoesNotExist, IndexError) as e:
        dompet = Dompet.objects.create(saldo=0)

    print(Dompet.objects.all())
    print(dompet)
    # arus_kas = ArusKas.objects.filter(dompet=dompet)
    arus_kas = ArusKas.objects.all()

    pemasukan, pengeluaran = 0, 0
    for arus in arus_kas:
        if arus.tipe == 1:
            pemasukan += arus.nominal
        else:
            pengeluaran += arus.nominal
    total = pemasukan - pengeluaran
    is_positive = total >= 0
    total = abs(total)

    data = {
        "saldo": dompet.saldo,
        "pemasukan": pemasukan,
        "pengeluaran": pengeluaran,
        "total": total,
        "is_positive": is_positive,
    }
    print(data)
    return JsonResponse(data)


def show_dompet_ajax(request, filter_type="all"):
    try:
        # dompet = Dompet.objects.get(user=request.user)
        dompet = Dompet.objects.all()[1]
    except (Dompet.DoesNotExist, IndexError) as e:
        dompet = Dompet.objects.create(saldo=0)

    # arus_kas = ArusKas.objects.filter(dompet=dompet)
    arus_kas = ArusKas.objects.all()
    if filter_type == "date":
        arus_kas = arus_kas.filter(created_at__date=datetime.date.today())
    elif filter_type == "week":
        arus_kas = arus_kas.filter(
            created_at__week=datetime.date.today().isocalendar()[1],
            created_at__year=datetime.date.today().isocalendar()[0],
            created_at__month__gte=datetime.date.today().month,
        )
    elif filter_type == "month":
        arus_kas = arus_kas.filter(created_at__month=datetime.date.today().month)
    elif filter_type == "year":
        arus_kas = arus_kas.filter(created_at__year=datetime.date.today().year)
    elif filter_type == "all":
        pass
    else:
        return JsonResponse({"status": "error"})

    pemasukan, pengeluaran = 0, 0
    for arus in arus_kas:
        if arus.tipe == 1:
            pemasukan += arus.nominal
        else:
            pengeluaran += arus.nominal
    total = pemasukan - pengeluaran
    is_positive = total >= 0
    total = abs(total)

    context = {
        "saldo": dompet.saldo,
        "pemasukan": pemasukan,
        "pengeluaran": pengeluaran,
        "total": total,
        "is_positive": is_positive,
    }
    return JsonResponse(context)


def show_arus_kas(request):
    # arus_kas = ArusKas.objects.filter(dompet__user=request.user)
    arus_kas = ArusKas.objects.all()

    pemasukan, pengeluaran = 0, 0
    for arus in arus_kas:
        if arus.tipe == 1:
            pemasukan += arus.nominal
        else:
            pengeluaran += arus.nominal
    total = pemasukan - pengeluaran
    is_positive = total >= 0
    total = abs(total)

    context = {
        "arus_kas": arus_kas,
        "pemasukan": pemasukan,
        "pengeluaran": pengeluaran,
        "total": total,
        "is_positive": is_positive,
    }
    return render(request, "arus_kas.html", context=context)


def show_arus_kas_json(request):
    # arus_kas = ArusKas.objects.filter(dompet__user=request.user)
    arus_kas = ArusKas.objects.all()
    arus_kas_json = serializers.serialize("json", arus_kas)
    return HttpResponse(arus_kas_json, content_type="application/json")


@csrf_exempt
def create_arus_kas(request):
    if request.method == "POST":
        try:
            # dompet = Dompet.objects.get(user=request.user)
            dompet = Dompet.objects.all()[1]
        except (Dompet.DoesNotExist, IndexError) as e:
            dompet = Dompet.objects.create(saldo=0)
        nominal = request.POST.get("nominal")
        keterangan = request.POST.get("keterangan")
        tipe = request.POST.get("tipe")
        temp_saldo = dompet.saldo + int(tipe) * int(nominal)
        print(keterangan, tipe, nominal, temp_saldo)

        if temp_saldo < 0:
            messages.error(request, "Saldo tidak boleh negatif!")
            # return redirect("dompet:show_dompet")
            return JsonResponse(
                {
                    "status": "error",
                    "message": "Saldo tidak boleh negatif!",
                },
                status=400,
            )

        dompet.saldo = temp_saldo
        dompet.save()
        arus_kas = ArusKas.objects.create(
            nominal=nominal, keterangan=keterangan, tipe=tipe
        )
        arus_kas.save()
        messages.success(request, "Arus kas berhasil dibuat!")
        # return redirect("dompet:show_dompet")
        return JsonResponse(
            {
                "status": "success",
                "message": "Arus kas berhasil dibuat!",
            },
            status=200,
        )
    return JsonResponse(
        {
            "status": "error",
            "message": "Method not allowed!",
        },
        status=405,
    )


#
# def create_arus_kas(request):
#     if request.method == "POST":
#         try:
#         except (Dompet.DoesNotExist, IndexError) as e:

#         form = ArusKasForm(request.POST)

#         if form.is_valid():
#             tipe = form.cleaned_data["tipe"]
#             nominal = form.cleaned_data["nominal"]
#             keterangan = form.cleaned_data["keterangan"]

#             temp_saldo = dompet.saldo + int(tipe) * int(nominal)

#             if temp_saldo < 0:
#                 messages.error(request, "Saldo tidak boleh negatif!")
#                 return redirect("dompet:show_dompet")

#             dompet.saldo = temp_saldo
#             dompet.save()
#             arus_kas = ArusKas.objects.create(
#             )
#             arus_kas.save()
#             messages.success(request, "Arus kas berhasil dibuat!")
#             return redirect("dompet:show_dompet")
#     else:
#         form = ArusKasForm()

#     return render(request, "dompet.html", {"form": form})


@csrf_exempt
def create_arus_kas_ajax(request):
    if request.method == "POST":
        try:
            # dompet = Dompet.objects.get(user=request.user)
            dompet = Dompet.objects.all()[1]
        except (Dompet.DoesNotExist, IndexError) as e:
            dompet = Dompet.objects.create(saldo=0)
        nominal = request.POST.get("nominal")
        keterangan = request.POST.get("keterangan")
        tipe = request.POST.get("tipe")
        temp_saldo = dompet.saldo + int(tipe) * int(nominal)
        if temp_saldo < 0:
            return JsonResponse(
                {"status": "error", "message": "Saldo tidak boleh negatif!"}
            )

        dompet.saldo = temp_saldo
        dompet.save()
        arus_kas = ArusKas.objects.create(
            nominal=nominal, keterangan=keterangan, tipe=tipe
        )
        arus_kas.save()
        resp = {
            "status": "success",
            "nominal": nominal,
            "keterangan": keterangan,
            "tipe": tipe,
            "created_at": arus_kas.created_at,
        }
        return JsonResponse(resp)

    return JsonResponse({"status": "error"})


def filter_arus_kas_ajax(request, filter_type):
    # arus_kas = ArusKas.objects.filter(dompet__user=request.user)
    arus_kas = ArusKas.objects.all()
    if filter_type == "date":
        arus_kas = arus_kas.filter(created_at__date=datetime.date.today())
    elif filter_type == "week":
        arus_kas = arus_kas.filter(
            created_at__week=datetime.date.today().isocalendar()[1],
            created_at__year=datetime.date.today().isocalendar()[0],
            created_at__month__gte=datetime.date.today().month,
        )
    elif filter_type == "month":
        arus_kas = arus_kas.filter(created_at__month=datetime.date.today().month)
    elif filter_type == "year":
        arus_kas = arus_kas.filter(created_at__year=datetime.date.today().year)
    elif filter_type == "reset":
        pass
    else:
        return JsonResponse({"status": "error"})

    pemasukan, pengeluaran = 0, 0
    for arus in arus_kas:
        if arus.tipe == 1:
            pemasukan += arus.nominal
        else:
            pengeluaran += arus.nominal
    total = pemasukan - pengeluaran
    is_positive = total >= 0
    total = abs(total)

    return HttpResponse(
        serializers.serialize("json", arus_kas), content_type="application/json"
    )
