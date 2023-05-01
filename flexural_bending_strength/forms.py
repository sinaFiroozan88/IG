from django import forms
from django.forms import widgets
from .models import Flexural_Bending_Strength_Model


class Flexural_Bending_strength_Form(forms.ModelForm):
    class Meta:
        model = Flexural_Bending_Strength_Model
        fields = {
            'author', 'year', 'month', 'day', 'code', 'f_flex', 'fm_flex', 'flexural_strength', 'f_compress',
            'fm_compress', 'compressive_strength'
        }
        widgets = {
            'author': forms.Select(),
            'year': forms.NumberInput(),
            'month': forms.NumberInput(),
            'day': forms.NumberInput(),
            'code': forms.Select(),
            'f_flex': forms.NumberInput(),
            'fm_flex': forms.NumberInput(),
            'flexural_Strength': forms.NumberInput(),
            'f_compress': forms.NumberInput(),
            'fm_compress': forms.NumberInput(),
            'compressive_strength': forms.NumberInput(),
        }
