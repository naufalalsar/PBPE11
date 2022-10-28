from django.urls import path, re_path
from donation.views import index, show_json, transaksi_donasi, add_donasi

app_name = 'donation'

urlpatterns = [
    path('', index, name='index'),
    path('add-donation/', add_donasi, name='add_donasi'),
    # # path('transaksi_donasi/', transaksi_donasi, name='transaksi_donasi'),
    
    path('transaksi_donasi/<str:id>/', transaksi_donasi, name='transaksi_donasi'),

    path('json/', show_json, name='show_json'),
]