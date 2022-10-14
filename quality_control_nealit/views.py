from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import View
from .forms import QualityControlForm
from . import models


class QualityControlView(View):
    def get(self, request):
        form = QualityControlForm()
        return render(request, 'quality_control/quality_control_new.html', {
            'form': form
        })

    def post(self, request):
        form = QualityControlForm(request.POST)
        if form.is_valid():
            qc_nealit_new = form.save(commit=False)
            qc_nealit_new.author = request.user
            qc_nealit_new.published_date = timezone.now()
            form.save()
            return redirect('quality_control_nealit_detail', pk=qc_nealit_new.pk)
        return render(request, 'quality_control/quality_control_new.html', {'form': form})


class QC_Nealit_Detail(View):
    def get(self, request, pk):
        qc_detail = get_object_or_404(models.QualityControlModel, pk=pk)
        context = {
            'detail': qc_detail
        }
        return render(request, 'quality_control/qc_nealit_detail.html', context)

    def post(self, request, pk):
        qc_detail = get_object_or_404(models.QualityControlModel, pk=pk)
        context = {
            'detail': qc_detail
        }
        return render(request, 'quality_control/qc_nealit_detail.html', context)


class QC_Nealit_Delete(View):
    def get(self, request, pk):
        product = get_object_or_404(models.QualityControlModel, pk=pk)
        product.delete()
        return redirect(reverse('quality_control_nealit_new'))

    def post(self, request, pk):
        product = get_object_or_404(models.QualityControlModel, pk=pk)
        product.delete()
        return redirect(reverse('quality_control_nealit_new'))


class QC_Nealit_Edit(View):
    def get(self, request, pk):
        qc_nealit_model = get_object_or_404(models.QualityControlModel, pk=pk)
        form = QualityControlForm(instance=qc_nealit_model)
        return render(request, 'quality_control/qc_nealit_edit.html', {'form': form})

    def post(self, request, pk):
        qc_nealit_model = get_object_or_404(models.QualityControlModel, pk=pk)
        form = QualityControlForm(request.POST, instance=qc_nealit_model)
        if form.is_valid():
            qc_nealit_model = form.save(commit=False)
            qc_nealit_model.author = request.user
            qc_nealit_model.published_date = timezone.now()
            qc_nealit_model.save()
            return redirect(f'/qc-nealit/detail/{pk}')
        return render(request, 'quality_control/qc_nealit_edit.html', {'form': form})


class QC_Nealit_List(View):
    def get(self, request):
        qc_nealit_list = models.QualityControlModel.objects.all().order_by('published_date')
        context = {
            'lists': qc_nealit_list
        }
        return render(request, 'quality_control/qc_nealit_list.html', context)

    def post(self, request):
        qc_nealit_list = models.QualityControlModel.objects.all().order_by('published_date')
        context = {
            'lists': qc_nealit_list
        }
        return render(request, 'quality_control/qc_nealit_list.html', context)
