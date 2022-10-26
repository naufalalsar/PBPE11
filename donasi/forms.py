
from donasi.models import Donasi
from django import forms

class DonasiForm(forms.ModelForm):
    class Meta:
        model = Donasi
        fields = ('user', 'title', 'description', 'start_date', 'end_date')
        exclude = ['user']