from django import forms
from .models import *

class AudioForm(forms.ModelForm):
    class Meta:
        model=songs
        fields=['title','template','song']

