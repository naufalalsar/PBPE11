from django.urls import path
from kurs.views import kurs

app_name = "kurs"

urlpatterns = [
    path('', kurs, name="kurs"),
]
