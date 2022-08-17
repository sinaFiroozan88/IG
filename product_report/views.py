from django.shortcuts import render
from django.views import View
from . import forms

from . import models


def ProductReport(request):
    form = forms.ProductReport
    return render(request, 'product_report/product_report.html', {
        'form': form
    })
