from django import forms
from django.forms import widgets
from .models import QC_Block_Stucco_Model


class QC_Block_Stucco_Form(forms.ModelForm):
    class Meta:
        model = QC_Block_Stucco_Model
        fields = {
            'author', 'month', 'day', 'hour', 'crystal_water_stucco', 'einstrumenge', 'water_gypsum_ratio',
            'initial_setting_time', 'final_setting_time', 'retained_200', 'retained_500', 'non_conformity',
            'action', 'remarks'
        }
        widgets = {
            'author': forms.Select(),
            'month': forms.NumberInput(),
            'day': forms.NumberInput(),
            'hour': forms.NumberInput(),
            'crystal_water_stucco': forms.NumberInput(),
            'einstrumenge': forms.NumberInput(),
            'water_gypsum_ratio': forms.NumberInput(),
            'initial_setting_time': forms.NumberInput(),
            'final_setting_time': forms.NumberInput(),
            'retained_200': forms.NumberInput(),
            'retained_500': forms.NumberInput(),
            'non_conformity': forms.Textarea(),
            'action': forms.Textarea(),
            'remarks': forms.Textarea(),
        }
