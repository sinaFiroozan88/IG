from django import forms
from django.forms import widgets
from .models import QC_Block_Model


class QC_Block_Form(forms.ModelForm):
    class Meta:
        model = QC_Block_Model
        fields = {
            'author', 'year', 'month', 'day', 'date_production', 'date_sampling', 'type_block', 'thickness', 'length',
            'height', 'flatness',
            'mass', 'surface_mass', 'density', 'water_absorption', 'ph', 'bending_strength', 'humidity', 'non_conformity', 'action',
            'remarks'
        }
        widgets = {
            'author': forms.Select(),
            'year': forms.NumberInput(),
            'month': forms.NumberInput(),
            'day': forms.NumberInput(),
            'date_production': forms.DateInput(attrs={'type': 'date'}),
            'date_sampling': forms.DateInput(attrs={'type': 'date'}),
            'type_block': forms.Select(),
            'thickness': forms.NumberInput(),
            'length': forms.NumberInput(),
            'height': forms.NumberInput(),
            'flatness': forms.Select(),
            'mass': forms.NumberInput(),
            'surface_mass': forms.NumberInput(),
            'density': forms.NumberInput(),
            'water_absorption': forms.NumberInput(),
            'ph': forms.NumberInput(),
            'bending_strength': forms.NumberInput(),
            'humidity': forms.NumberInput(),
            'non_conformity': forms.Textarea(),
            'action': forms.Textarea(),
            'remarks': forms.Textarea(),
        }
