from django.urls import path
from kurs.views import kurs, kurs_json, calculate, chart

app_name = "kurs"

urlpatterns = [
    path("", kurs, name="kurs"),
    path("json/<str:currency>", kurs_json, name="kurs_json"),
    path("calculate", calculate, name="calculate"),
    path("chart/<str:source_currency>/<str:target_currency>", chart, name="chart"),
]
