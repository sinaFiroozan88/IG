from django import forms
from django.forms import widgets
from .models import Avg_Test_Production_Model


class Avg_Test_Production_Form(forms.ModelForm):
    class Meta:
        model = Avg_Test_Production_Model
        fields = {
            'author', 'year', 'month', 'day', 'line', 'product_silo', 'usage', 'free_moisture', 'crystal_water_raw_mat',
            'purity_of_raw_material', 'crystal_water_of_stucco', 'einstrumenge',
            'water_gypsum_ratio', 'initial_setting_time', 'final_setting_time', 'retained_on_63', 'retained_on_200',
            'retained_on_500', 'remarks'
        }
        widgets = {
            'author': forms.Select(),
            'year': forms.NumberInput(),
            'month': forms.NumberInput(),
            'day': forms.NumberInput(),
            'line': forms.Select(),
            'product_silo': forms.Select(),
            'usage': forms.NumberInput(),
            'free_moisture': forms.NumberInput(),
            'crystal_water_raw_mat': forms.NumberInput(),
            'purity_of_raw_material': forms.NumberInput(),
            'crystal_water_of_stucco': forms.NumberInput(),
            'water_gypsum_ratio': forms.NumberInput(),
            'initial_setting_time': forms.NumberInput(),
            'final_setting_time': forms.NumberInput(),
            'retained_on_63': forms.NumberInput(),
            'retained_on_200': forms.NumberInput(),
            'retained_on_500': forms.NumberInput(),
            'remarks': forms.Textarea(),
        }
