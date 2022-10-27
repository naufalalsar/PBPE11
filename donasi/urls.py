from django.urls import path
from donasi.views import index, add_donasi

app_name = 'donasi'

urlpatterns = [
    path('', index, name='index'),
    path('add-donasi/', add_donasi, name='add-donasi'),

]