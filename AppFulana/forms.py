from django import forms

class PosteosForm(forms.Form):
    titulo = forms.CharField()
    contanos = forms.CharField(max_length=8000)

class LenguajeForm(forms.Form):
    lenguaje = forms.CharField()
    review = forms.CharField(max_length=8000)

class InstitutoForm(forms.Form):
    instituto = forms.CharField()
    review = forms.CharField(max_length=8000)