from django import forms
from django.forms import widgets
from .models import Blane_Model


class Blane_Form(forms.ModelForm):
    class Meta:
        model = Blane_Model
        fields = {
            'number', 'author', 'published_date', 'blane', 'initial_setting_time', 'final_setting_time'
        }
        widgets = {
            'number': forms.NumberInput(),
            'author': forms.Select(),
            'published_date': forms.DateInput(attrs={'type': 'date'}),
            'blane': forms.NumberInput(),
            'initial_setting_time': forms.NumberInput(),
            'final_setting_time': forms.NumberInput(),
        }
