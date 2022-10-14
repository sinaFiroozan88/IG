from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from . import models
from .forms import QC_Block_Form
from django.views import View
from . import forms


class QC_Block_New(View):
    def get(self, request):
        form = forms.QC_Block_Form()
        return render(request, 'qc_block/qc_block_new.html', {
            'form': form
        })

    def post(self, request):
        form = forms.QC_Block_Form(request.POST)
        if form.is_valid():
            qc_block = form.save(commit=False)
            qc_block.author = request.user
            qc_block.published_date = timezone.now()
            form.save()
            return redirect('qc_block_detail', pk=qc_block.pk)

        return render(request, 'qc_block/qc_block_new.html', {
            'form': form
        })


class QC_Block_Detail(View):
    def get(self, request, pk):
        qc_block_detail = get_object_or_404(models.QC_Block_Model, pk=pk)
        context = {
            'detail': qc_block_detail
        }
        return render(request, 'qc_block/qc_block_detail.html', context)

    def post(self, request, pk):
        qc_block_detail = get_object_or_404(models.QC_Block_Model, pk=pk)
        context = {
            'detail': qc_block_detail
        }
        return render(request, 'qc_block/qc_block_detail.html', context)


class QC_Block_List(View):
    def get(self, request):
        qc_block_list = models.QC_Block_Model.objects.all().order_by('published_date')
        context = {
            'lists': qc_block_list
        }
        return render(request, 'qc_block/qc_block_list.html', context)

    def post(self, request):
        qc_block_list = models.QC_Block_Model.objects.all().order_by('published_date')
        context = {
            'lists': qc_block_list
        }
        return render(request, 'qc_block/qc_block_list.html', context)


class QC_Blcok_Delete(View):
    def get(self, request, pk):
        qc_block_model = get_object_or_404(models.QC_Block_Model, pk=pk)
        qc_block_model.delete()
        return redirect(reverse('qc_block_new'))

    def post(self, request, pk):
        qc_block_model = get_object_or_404(models.QC_Block_Model, pk=pk)
        qc_block_model.delete()
        return redirect(reverse('qc_block_new'))


class QC_Block_Edit(View):
    def get(self, request, pk):
        qc_block_model = get_object_or_404(models.QC_Block_Model, pk=pk)
        form = QC_Block_Form(instance=qc_block_model)
        return render(request, 'qc_block/qc_block_edit.html', {'form': form})

    def post(self, request, pk):
        qc_block_model = get_object_or_404(models.QC_Block_Model, pk=pk)
        form = QC_Block_Form(request.POST, instance=qc_block_model)
        if form.is_valid():
            qc_block_model = form.save(commit=False)
            qc_block_model.author = request.user
            qc_block_model.published_date = timezone.now()
            qc_block_model.save()
            return redirect(f'/qc-block/detail/{pk}')
        return render(request, 'qc_block/qc_block_edit.html', {'form': form})
