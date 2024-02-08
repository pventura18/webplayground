from django import forms

from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la página'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Orden de la página'}),
        }
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'order': 'Orden',
        }
        