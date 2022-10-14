from django import forms
from django.forms import widgets
from .models import Ten_Sieve_Analysis


class QC_Block_Stucco_Form(forms.ModelForm):
    class Meta:
        model = Ten_Sieve_Analysis
        fields = {
            'author', 'year', 'month', 'day', 'sieve_40', 'sieve_63', 'sieve_90', 'sieve_100', 'sieve_200', 'sieve_300', 'sieve_400', 'sieve_500',
            'sieve_600', 'sieve_1000'
        }
        widgets = {
            'author': forms.Select(),
            'year': forms.NumberInput(),
            'month': forms.NumberInput(),
            'day': forms.NumberInput(),
            'sieve_40': forms.NumberInput(),
            'sieve_63': forms.NumberInput(),
            'sieve_90': forms.NumberInput(),
            'sieve_100': forms.NumberInput(),
            'sieve_200': forms.NumberInput(),
            'sieve_300': forms.NumberInput(),
            'sieve_400': forms.NumberInput(),
            'sieve_500': forms.NumberInput(),
            'sieve_600': forms.NumberInput(),
            'sieve_1000': forms.NumberInput(),
        }
