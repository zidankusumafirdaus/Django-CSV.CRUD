from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'price']

class CSVUploadForm(forms.Form):
    file = forms.FileField()
