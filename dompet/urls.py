from django.urls import path
from dompet.views import *

app_name = "dompet"

urlpatterns = [
    path('', show_dompet, name="show_dompet"),
]