from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from . import models
from .forms import Ultrax_Form
from django.views import View
from . import forms


class Ultrax_New(View):
    def get(self, request):
        form = forms.Ultrax_Form()
        return render(request, 'ultrax_calibration/ultrax_new.html', {
            'form': form
        })

    def post(self, request):
        form = forms.Ultrax_Form(request.POST)
        if form.is_valid():
            ultrax_calibration = form.save(commit=False)
            ultrax_calibration.author = request.user
            ultrax_calibration.published_date = timezone.now()
            form.save()
            return redirect('ultrax_calibration_detail', pk=ultrax_calibration.pk)
        return render(request, 'ultrax_calibration/ultrax_new.html', {
            'form': form
        })


class Ultrax_Detail(View):
    def get(self, request, pk):
        ultrax_detail = get_object_or_404(models.Ultrax_Model, pk=pk)
        context = {
            'detail': ultrax_detail
        }
        return render(request, 'ultrax_calibration/ultrax_detail.html', context)

    def post(self, request, pk):
        ultrax_detail = get_object_or_404(models.Ultrax_Model, pk=pk)
        context = {
            'detail': ultrax_detail
        }
        return render(request, 'ultrax_calibration/ultrax_detail.html', context)


class Ultrax_List(View):
    def get(self, request):
        ultrax_calibration_list = models.Ultrax_Model.objects.all().order_by('published_date')
        context = {
            'lists': ultrax_calibration_list
        }
        return render(request, 'ultrax_calibration/ultrax_list.html', context)

    def post(self, request):
        ultrax_calibration_list = models.Ultrax_Model.objects.all().order_by('published_date')
        context = {
            'lists': ultrax_calibration_list
        }
        return render(request, 'ultrax_calibration/ultrax_list.html', context)


class Ultrax_Delete(View):
    def get(self, request, pk):
        ultrax_model = get_object_or_404(models.Ultrax_Model, pk=pk)
        ultrax_model.delete()
        return redirect(reverse('ultrax_calibration_new'))

    def post(self, request, pk):
        ultrax_model = get_object_or_404(models.Ultrax_Model, pk=pk)
        ultrax_model.delete()
        return redirect(reverse('ultrax_calibration_new'))


class Ultrax_Edit(View):
    def get(self, request, pk):
        ten_sieve_analyse_model = get_object_or_404(models.Ultrax_Model, pk=pk)
        form = Ultrax_Form(instance=ten_sieve_analyse_model)
        return render(request, 'ultrax_calibration/ultrax_edit.html', {'form': form})

    def post(self, request, pk):
        ultrax_calibration_model = get_object_or_404(models.Ultrax_Model, pk=pk)
        form = Ultrax_Form(request.POST, instance=ultrax_calibration_model)
        if form.is_valid():
            ultrax_calibration_form = form.save(commit=False)
            ultrax_calibration_form.author = request.user
            ultrax_calibration_form.published_date = timezone.now()
            ultrax_calibration_form.save()
            return redirect(f'/ultrax-calibration/detail/{pk}')
        return render(request, 'ultrax_calibration/ultrax_edit.html', {'form': form})
