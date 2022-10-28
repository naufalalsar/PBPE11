from django.urls import path
from berita.views import *

app_name = 'berita'

urlpatterns = [
    path('add/', add, name='add'),
    path('', show, name='show'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('json/', json_all, name='json_all'),
    path('show/<int:pk>', berita, name='berita'),
    path('delete_filter/<int:pk>', delete_filter, name="delete_filter")
]