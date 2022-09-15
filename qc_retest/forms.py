from django import forms
from django.forms import widgets
from .models import QC_Retest_Model


class QC_Retest_Form(forms.ModelForm):
    class Meta:
        model = QC_Retest_Model
        fields = {
            'author', 'year', 'month', 'day', 'hour', 'line', 'product_silo', 'mine', 'free_moisture',
            'crystal_water_raw_mat',
            'Purity_raw_mat',
            'crystal_water_stucco',
            'Einstrumenge', 'Water_gypsum_ratio', 'initial_setting_time', 'final_setting_time', 'retained_on_63',
            'retained_on_200',
            'retained_on_500', 'non_conformity', 'actions', 'remarks'
        }
        widgets = {
            'author': forms.Select(),
            'year': forms.NumberInput(),
            'month': forms.NumberInput(),
            'day': forms.NumberInput(),
            'hour': forms.NumberInput(),
            'line': forms.Select(),
            'product_silo': forms.Select(),
            'mine': forms.Select(),
            'free_moisture': forms.NumberInput(),
            'crystal_water_raw_mat': forms.NumberInput(),
            'Purity_raw_mat': forms.NumberInput(),
            'crystal_water_stucco': forms.NumberInput(),
            'Einstrumenge': forms.NumberInput(),
            'Water_gypsum_ratio': forms.NumberInput(),
            'initial_setting_time': forms.NumberInput(),
            'final_setting_time': forms.NumberInput(),
            'retained_on_63': forms.NumberInput(),
            'retained_on_200': forms.NumberInput(),
            'retained_on_500': forms.NumberInput(),
            'non_conformity': forms.Textarea(),
            'actions': forms.Textarea(),
            'remarks': forms.Textarea(),
        }
