from django import forms
from django.forms import widgets
from .models import QualityControlModel


class QualityControlForm(forms.ModelForm):
    class Meta:
        model = QualityControlModel
        fields = {
            'author', 'year', 'month', 'day', 'hour', 'inlet_feed', 'bag_number_2', 'bag_number',
            'free_moisture_filterdust', 'crystal_water_filterdust', 'purity_filterdust', 'free_moisture_nealit',
            'retained_on_63', 'retained_on_200',
            'retained_on_500', 'blaine_Nealit', 'blaine_filterdust', 'blaine_after_mill', 'remarks', }
        widgets = {
            'author': forms.Select(),
            'year': forms.NumberInput(),
            'month': forms.NumberInput(),
            'day': forms.NumberInput(),
            'hour': forms.NumberInput(),
            'inlet_feed': forms.Select(),
            'bag_number_2': forms.NumberInput(),
            'bag_number': forms.DateInput(attrs={'type': 'date'}),
            'free_moisture_filterdust': forms.NumberInput(),
            'crystal_water_filterdust': forms.NumberInput(),
            'purity_filterdust': forms.NumberInput(),
            'free_moisture_nealit': forms.NumberInput(),
            'retained_on_63': forms.NumberInput(),
            'retained_on_200': forms.NumberInput(),
            'retained_on_500': forms.NumberInput(),
            'blaine_Nealit': forms.NumberInput(),
            'blaine_filterdust': forms.NumberInput(),
            'blaine_after_mill': forms.NumberInput(),
            'remarks': forms.Textarea()
        }
