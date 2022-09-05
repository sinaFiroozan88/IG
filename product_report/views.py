from django.db.transaction import commit
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView
from . import forms
from . import models
from django.contrib.auth.decorators import login_required


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
            return redirect(reverse('product_report_list'))
        else:
            return redirect(reverse('product_report'))


@login_required
def ProductReportList(request):
    product_report_list = models.ProductReport.objects.all().order_by('Published_Date')
    context = {
        'lists': product_report_list
    }
    return render(request, 'product_report/product_report_list.html', context)


@login_required
def ProductReportDetail(request, pk):
    product_report_detail = get_object_or_404(models.ProductReport, pk=pk)
    return render(request, 'product_report/product_report_detail.html', {
        'detail': product_report_detail
    })


@login_required
def ProductReportDelete(request, pk):
    product_report = get_object_or_404(models.ProductReport, pk=pk)
    product_report.delete()
    return redirect(reverse('product_report_list'))


@login_required
def ProductReportEdit(request, pk):
    product_report = get_object_or_404(models.ProductReport, pk=pk)
    if request.method == "POST":
        form = forms.ProductReportForm(request.POST, instance=product_report)
        if form.is_valid():
            product_report = form.save(commit=False)
            product_report.author = request.user
            product_report.Published_Date = timezone.now()
            product_report.save()
            return redirect(f'/product_report_detail/{pk}')
        else:
            pass
        return render(request, 'product_report/product_report_edit.html', {
            'form': form
        })
    else:
        form = forms.ProductReportForm(instance=product_report)
        return render(request, 'product_report/product_report_edit.html', {'form': form})
