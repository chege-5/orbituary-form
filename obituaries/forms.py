from django import forms
from .models import Obituary

class ObituaryForm(forms.ModelForm):
    class Meta:
        model = Obituary
        fields = ['name', 'id', 'date_of_birth', 'date_of_death', 'title', 'content', 'author']
       