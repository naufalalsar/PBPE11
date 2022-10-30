from django import forms
from forum.models import Forum

class ForumForm(forms.Form):
    judul = forms.CharField(max_length=200)
    isi = forms.CharField(widget=forms.Textarea)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ForumForm, self).__init__(*args, **kwargs)

    def save(self):
        Forum(user=self.user, judul=self.cleaned_data['judul'], isi=self.cleaned_data['isi']).save()


    

