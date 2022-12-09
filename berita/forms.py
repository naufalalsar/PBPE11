from django import forms
from berita.models import Berita

CHOICES=[('uang','Uang'),
         ('bank','Bank'),
          ('ekonomi','Ekonomi'),
           ('kripto','Kripto'),
            ('saham','Saham')]

class BeritaForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    category = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    writer = forms.CharField(max_length=200)
    source = forms.CharField(max_length=200)

    def __init__(self, user, *args, **kwargs):
        super(BeritaForm, self).__init__(*args, **kwargs)

    def save(self):
        Berita(title=self.cleaned_data['title'], content=self.cleaned_data['content'], category=self.cleaned_data['category'], writer=self.cleaned_data['writer'], source=self.cleaned_data['source']).save()


    
