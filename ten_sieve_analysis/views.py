from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from . import models
from .forms import QC_Block_Stucco_Form
from django.views import View
from . import forms


# class QC_Block_Stucco_New(View):
#     def get(self, request):
#         form = forms.QC_Block_Stucco_Form()
#         return render(request, 'qc_block_stucco/qc_block_stucco_new.html', {
#             'form': form
#         })
#
#     def post(self, request):
#         form = forms.QC_Block_Stucco_Form(request.POST)
#         if form.is_valid():
#             qc_block_stucco = form.save(commit=False)
#             qc_block_stucco.author = request.user
#             qc_block_stucco.published_date = timezone.now()
#             form.save()
#             # return redirect('qc_block_detail', pk=qc_block_stucco.pk)
#             return redirect('qc_block_stucco_detail', pk=qc_block_stucco.pk)
#
#         return render(request, 'qc_block_stucco/qc_block_stucco_new.html', {
#             'form': form
#         })
#
# class QC_Block_Stucco_Detail(View):
#     def get(self, request, pk):
#         qc_block_stucco_detail = get_object_or_404(models.QC_Block_Stucco_Model, pk=pk)
#         context = {
#             'detail': qc_block_stucco_detail
#         }
#         return render(request, 'qc_block_stucco/qc_block_stucco_detail.html', context)
#
#     def post(self, request, pk):
#         qc_block_stucco_detail = get_object_or_404(models.QC_Block_Stucco_Model, pk=pk)
#         context = {
#             'detail': qc_block_stucco_detail
#         }
#         return render(request, 'qc_block_stucco/qc_block_stucco_detail.html', context)
#
#
# class QC_Block_Stucco_List(View):
#     def get(self, request):
#         qc_block_stucco_list = models.QC_Block_Stucco_Model.objects.all().order_by('published_date')
#         context = {
#             'lists': qc_block_stucco_list
#         }
#         return render(request, 'qc_block_stucco/qc_block_stucco_list.html', context)
#
#     def post(self, request):
#         qc_block_stucco_list = models.QC_Block_Stucco_Model.objects.all().order_by('published_date')
#         context = {
#             'lists': qc_block_stucco_list
#         }
#         return render(request, 'qc_block_stucco/qc_block_stucco_list.html', context)
#
#
# class QC_Block_Stucco_Delete(View):
#     def get(self, request, pk):
#         qc_block_stucco_model = get_object_or_404(models.QC_Block_Stucco_Model, pk=pk)
#         qc_block_stucco_model.delete()
#         return redirect(reverse('qc_block_stucco_new'))
#
#     def post(self, request, pk):
#         qc_block_stucco_model = get_object_or_404(models.QC_Block_Stucco_Model, pk=pk)
#         qc_block_stucco_model.delete()
#         return redirect(reverse('qc_block_stucco_new'))
#
# #
# class QC_Block_Stucco_Edit(View):
#     def get(self, request, pk):
#         qc_block_model = get_object_or_404(models.QC_Block_Stucco_Model, pk=pk)
#         form = QC_Block_Stucco_Form(instance=qc_block_model)
#         return render(request, 'qc_block_stucco/qc_block_stucco_edit.html', {'form': form})
#
#     def post(self, request, pk):
#         qc_block_model = get_object_or_404(models.QC_Block_Stucco_Model, pk=pk)
#         form = QC_Block_Stucco_Form(request.POST, instance=qc_block_model)
#         if form.is_valid():
#             qc_block_model = form.save(commit=False)
#             qc_block_model.author = request.user
#             qc_block_model.published_date = timezone.now()
#             qc_block_model.save()
#             return redirect(f'/qc-block-stucco/detail/{pk}')
#         return render(request, 'qc_block_stucco/qc_block_stucco_edit.html', {'form': form})
