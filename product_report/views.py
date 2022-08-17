from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from . import forms

from . import models


class ProductReport(View):
    def get(self, request):
        form = forms.ProductReportForm
        context = {
            'form': form
        }
        return render(request, 'product_report/product_report.html', context)

    def post(self, request):

        form = forms.ProductReportForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect(reverse('home_page'))
        else:
            return redirect(reverse('home_page'))
