from django import forms


class ArusKasForm(forms.Form):
    tipe = forms.IntegerField()
    nominal = forms.IntegerField()
    keterangan = forms.CharField(max_length=255)
