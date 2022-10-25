from django.urls import path
from donasi.views import index

app_name = 'donasi'

urlpatterns = [
    path('', index, name='index'),
]