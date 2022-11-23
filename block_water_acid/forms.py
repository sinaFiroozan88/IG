from django import forms
from django.forms import widgets
from .models import Block_Water_Acid_Model


class Block_Water_Acid_Form(forms.ModelForm):
    class Meta:
        model = Block_Water_Acid_Model
        fields = {
            'author', 'year', 'month', 'day', 'ph'
        }
        widgets = {
            'author': forms.Select(),
            'year': forms.NumberInput(),
            'month': forms.NumberInput(),
            'day': forms.NumberInput(),
            'ph': forms.NumberInput(),
        }