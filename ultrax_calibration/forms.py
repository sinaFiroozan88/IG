from django import forms
from django.forms import widgets
from .models import Ultrax_Model


class Ultrax_Form(forms.ModelForm):
    class Meta:
        model = Ultrax_Model
        fields = {
            'Target_Product', 'author', 'year', 'month', 'day', 'hour', 'line_qc', 'office_qa', 'kiln', 'dif_line_kiln', 'dif_qa_kiln'
        }
        widgets = {
            'Target_Product': forms.Select(),
            'author': forms.Select(),
            'year': forms.NumberInput(),
            'month': forms.NumberInput(),
            'day': forms.NumberInput(),
            'hour': forms.NumberInput(),
            'line_qc': forms.NumberInput(),
            'office_qz': forms.NumberInput(),
            'kiln': forms.NumberInput(),
            'dif_line_kiln': forms.NumberInput(),
            'dif_qa_kiln': forms.NumberInput(),
        }
