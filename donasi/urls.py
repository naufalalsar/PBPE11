from django.urls import path, re_path
from donasi.views import index, add_donasi, show_json, transaksi_donasi

app_name = 'donasi'

urlpatterns = [
    path('', index, name='index'),
    path('add-donasi/', add_donasi, name='add_donasi'),
    # path('transaksi_donasi/', transaksi_donasi, name='transaksi_donasi'),
    
    path('transaksi_donasi/<str:id>/', transaksi_donasi, name='transaksi_donasi'),

    path('json/', show_json, name='show_json'),
]