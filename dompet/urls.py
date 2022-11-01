from django.urls import path
from dompet.views import *

app_name = "dompet"

urlpatterns = [
    path("", show_dompet, name="show_dompet"),
    path("<str:filter_type>", show_dompet, name="show_dompet"),
    path("create_arus_kas/", create_arus_kas, name="create_arus_kas"),
    path(
        "create_arus_kas_ajax/",
        create_arus_kas_ajax,
        name="create_arus_kas_ajax",
    ),
    path("arus_kas/", show_arus_kas, name="show_arus_kas"),
    path("arus_kas/arus_kas_json/", show_arus_kas_json, name="show_arus_kas_json"),
    path(
        "arus_kas/filter_arus_kas_ajax/<str:filter_type>",
        filter_arus_kas_ajax,
        name="filter_arus_kas_ajax",
    ),
]
