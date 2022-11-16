from django import forms
from django.forms import widgets
from .models import Silis_Model


class Silis_Form(forms.ModelForm):
    class Meta:
        model = Silis_Model
        fields = {
            'author', 'target_product', 'year', 'month', 'day', 'hour', 'free_moisture',
            'crystal_water_rawmat', 'purity_rawmat', 'sio2'
        }
        widgets = {
            'author': forms.Select(),
            'target_product': forms.Select(),
            'year': forms.NumberInput(),
            'month': forms.NumberInput(),
            'day': forms.NumberInput(),
            'hour': forms.NumberInput(),
            'free_moisture': forms.NumberInput(),
            'crystal_water_rawmat': forms.NumberInput(),
            'purity_rawmat': forms.NumberInput(),
            'sio2': forms.NumberInput(),
        }
