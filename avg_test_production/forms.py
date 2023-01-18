from django import forms
from django.forms import widgets
from .models import Avg_Test_Production_Model

class Avg_Test_Production_Form(forms.ModelForm):
    class Meta:
        model = Avg_Test_Production_Model
        fields = {
            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
        }
        widgets = {

        }