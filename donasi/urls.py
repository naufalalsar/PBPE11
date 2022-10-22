from django.urls import path
from example_app.views import index

app_name = 'donasi'

urlpatterns = [
    path('', index, name='index'),
]