from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from . import models
from .forms import QC_Retest_Form
from django.views import View
from . import forms


class QC_Retest_New(View):
    def get(self, request):
        form = forms.QC_Retest_Form()
        return render(request, 'qc_retest/qc_retest_new.html', {
            'form': form
        })

    def post(self, request):
        form = forms.QC_Retest_Form(request.POST)
        if form.is_valid():
            qc_retest = form.save(commit=False)
            qc_retest.author = request.user
            qc_retest.publishe_date = timezone.now()
            form.save()
            return redirect('quality_control_retest_detail', pk=qc_retest.pk)

        return render(request, 'qc_retest/qc_retest_new.html', {
            'form': form
        })


class QC_Retest_Detail(View):
    def get(self, request, pk):
        qc_retest_detail = get_object_or_404(models.QC_Retest_Model, pk=pk)
        context = {
            'detail': qc_retest_detail
        }
        return render(request, 'qc_retest/qc_retest_detail.html', context)

    def post(self, request, pk):
        qc_retest_detail = get_object_or_404(models.QC_Retest_Model, pk=pk)
        context = {
            'detail': qc_retest_detail
        }
        return render(request, 'qc_retest/qc_retest_detail.html', context)


class QC_Retest_List(View):
    def get(self, request):
        qc_retest_list = models.QC_Retest_Model.objects.all().order_by('published_date')
        context = {
            'lists': qc_retest_list
        }
        return render(request, 'qc_retest/qc_retest_list.html', context)

    def post(self, request):
        qc_retest_list = models.QC_Retest_Model.objects.all().order_by('published_date')
        context = {
            'lists': qc_retest_list
        }
        return render(request, 'qc_retest/qc_retest_list.html', context)


class QC_Retest_Delete(View):
    def get(self, request, pk):
        qc_retest_model = get_object_or_404(models.QC_Retest_Model, pk=pk)
        qc_retest_model.delete()
        return redirect(reverse('quality_control_retest_new'))

    def post(self, request, pk):
        qc_retest_model = get_object_or_404(models.QC_Retest_Model, pk=pk)
        qc_retest_model.delete()
        return redirect(reverse('quality_control_retest_new'))


class QC_Retest_Edit(View):
    def get(self, request, pk):
        qc_retest_model = get_object_or_404(models.QC_Retest_Model, pk=pk)
        form = QC_Retest_Form(instance=qc_retest_model)
        return render(request, 'qc_retest/qc_retest_edit.html', {'form': form})

    def post(self, request, pk):
        qc_retest_model = get_object_or_404(models.QC_Retest_Model, pk=pk)
        form = QC_Retest_Form(request.POST, instance=qc_retest_model)
        if form.is_valid():
            qc_retest_model = form.save(commit=False)
            qc_retest_model.author = request.user
            qc_retest_model.published_date = timezone.now()
            qc_retest_model.save()
            return redirect(f'/qc-retest/detail/{pk}')
        return render(request, 'qc_retest/qc_retest_edit.html', {'form': form})
