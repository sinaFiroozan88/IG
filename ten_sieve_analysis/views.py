from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from . import models
from .forms import Ten_Sieve_Analyse_Form
from django.views import View
from . import forms


class Ten_Sieve_Analyse_New(View):
    def get(self, request):
        form = forms.Ten_Sieve_Analyse_Form()
        return render(request, 'ten_sieve_analyse/ten_sieve_analyse_new.html', {
            'form': form
        })

    def post(self, request):
        form = forms.Ten_Sieve_Analyse_Form(request.POST)
        if form.is_valid():
            ten_sieve_analyse = form.save(commit=False)
            ten_sieve_analyse.author = request.user
            ten_sieve_analyse.published_date = timezone.now()
            form.save()
            return redirect('ten_sieve_analyse_detail', pk=ten_sieve_analyse.pk)

        return render(request, 'ten_sieve_analyse/ten_sieve_analyse_new.html', {
            'form': form
        })

class Ten_Sieve_Analyse_Detail(View):
    def get(self, request, pk):
        ten_sieve_analyse_detail = get_object_or_404(models.Ten_Sieve_Analysis_Model, pk=pk)
        context = {
            'detail': ten_sieve_analyse_detail
        }
        return render(request, 'ten_sieve_analyse/ten_sieve_analyse_detail.html', context)

    def post(self, request, pk):
        ten_sieve_analyse_detail = get_object_or_404(models.Ten_Sieve_Analysis_Model, pk=pk)
        context = {
            'detail': ten_sieve_analyse_detail
        }
        return render(request, 'ten_sieve_analyse/ten_sieve_analyse_detail.html', context)


class Ten_Sieve_Analyse_List(View):
    def get(self, request):
        ten_sieve_analyse_list = models.Ten_Sieve_Analysis_Model.objects.all().order_by('published_date')
        context = {
            'lists': ten_sieve_analyse_list
        }
        return render(request, 'ten_sieve_analyse/ten_sieve_analyse_list.html', context)

    def post(self, request):
        ten_sieve_analyse_list = models.Ten_Sieve_Analysis_Model.objects.all().order_by('published_date')
        context = {
            'lists': ten_sieve_analyse_list
        }
        return render(request, 'ten_sieve_analyse/ten_sieve_analyse_list.html', context)


class Ten_Sieve_Analyse_Delete(View):
    def get(self, request, pk):
        ten_sieve_analyse_model = get_object_or_404(models.Ten_Sieve_Analysis_Model, pk=pk)
        ten_sieve_analyse_model.delete()
        return redirect(reverse('ten_sieve_analyse_new'))

    def post(self, request, pk):
        ten_sieve_analyse_model = get_object_or_404(models.Ten_Sieve_Analysis_Model, pk=pk)
        ten_sieve_analyse_model.delete()
        return redirect(reverse('ten_sieve_analyse_new'))


class Ten_Sieve_Analyse_Edit(View):
    def get(self, request, pk):
        ten_sieve_analyse_model = get_object_or_404(models.Ten_Sieve_Analysis_Model, pk=pk)
        form = Ten_Sieve_Analyse_Form(instance=ten_sieve_analyse_model)
        return render(request, 'ten_sieve_analyse/ten_sieve_analyse_edit.html', {'form': form})

    def post(self, request, pk):
        ten_sieve_analyse_model = get_object_or_404(models.Ten_Sieve_Analysis_Model, pk=pk)
        form = Ten_Sieve_Analyse_Form(request.POST, instance=ten_sieve_analyse_model)
        if form.is_valid():
            ten_sieve_analyse_model = form.save(commit=False)
            ten_sieve_analyse_model.author = request.user
            ten_sieve_analyse_model.published_date = timezone.now()
            ten_sieve_analyse_model.save()
            return redirect(f'/ten-sieve-analyse/detail/{pk}')
        return render(request, 'ten_sieve_analyse/ten_sieve_analyse_edit.html', {'form': form})
