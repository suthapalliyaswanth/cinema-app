from django import forms
from .models import cinema

class NoteForm(forms.ModelForm):
    class Meta:
        model = cinema
        fields = ['name','description','poster','genre','year_of_release','duration','cast','crew','rating']