from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from . import models
from django.views import View
from . import forms


class Flexural_Bending_Strength_New(View):
    def get(self, request):
        form = forms.Flexural_Bending_strength_Form()
        return render(request, 'flexural_bending_strength/flexural_bending_strength_new.html', {
            'form': form
        })

    def post(self, request):
        form = forms.Flexural_Bending_strength_Form(request.POST)
        if form.is_valid():
            flexural_bending_strength = form.save(commit=False)
            flexural_bending_strength.author = request.user
            flexural_bending_strength.published_date = timezone.now()
            form.save()
            # return redirect('ten_sieve_analyse_detail', pk=ten_sieve_analyse.pk)
            return redirect('home_page')
        return render(request, 'flexural_bending_strength/flexural_bending_strength_new.html', {
            'form': form
        })


class Flexural_Bending_Strength_Detail(View):
    def get(self, request, pk):
        flexural_bending_strength_detail = get_object_or_404(models.Flexural_Bending_Strength_Model, pk=pk)
        context = {
            'detail': flexural_bending_strength_detail
        }
        return render(request, 'flexural_bending_strength/flexural_bending_strength_detail.html', context)

    def post(self, request, pk):
        flexural_bending_strength_detail = get_object_or_404(models.Flexural_Bending_Strength_Model, pk=pk)
        context = {
            'detail': flexural_bending_strength_detail
        }
        return render(request, 'flexural_bending_strength/flexural_bending_strength_detail.html', context)


class Flexural_Bending_Strength_List(View):
    def get(self, request):
        flexural_bending_strength = models.Flexural_Bending_Strength_Model.objects.all().order_by('published_date')
        context = {
            'lists': flexural_bending_strength
        }
        return render(request, 'flexural_bending_strength/flexural_bending_strength_list.html', context)

    def post(self, request):
        flexural_bending_strength = models.Flexural_Bending_Strength_Model.objects.all().order_by('published_date')
        context = {
            'lists': flexural_bending_strength
        }
        return render(request, 'flexural_bending_strength/flexural_bending_strength_list.html', context)


class Flexural_Bending_Strength_Delete(View):
    def get(self, request, pk):
        flexural_bending_strength_model = get_object_or_404(models.Flexural_Bending_Strength_Model, pk=pk)
        flexural_bending_strength_model.delete()
        return redirect(reverse('flexural_bending_strength_new'))

    def post(self, request, pk):
        flexural_bending_strength_model = get_object_or_404(models.Flexural_Bending_Strength_Model, pk=pk)
        flexural_bending_strength_model.delete()
        return redirect(reverse('flexural_bending_strength_new'))


class Flexural_Bending_Strength_Edit(View):
    def get(self, request, pk):
        flexural_bending_strength_model = get_object_or_404(models.Flexural_Bending_Strength_Model, pk=pk)
        form = forms.Flexural_Bending_strength_Form(instance=flexural_bending_strength_model)
        return render(request, 'flexural_bending_strength/flexural_bending_strength_edit.html', {'form': form})

    def post(self, request, pk):
        flexural_bending_strength_model = get_object_or_404(models.Flexural_Bending_Strength_Model, pk=pk)
        form = forms.Flexural_Bending_strength_Form(request.POST, instance=flexural_bending_strength_model)
        if form.is_valid():
            flexural_bending_strength_model = form.save(commit=False)
            flexural_bending_strength_model.author = request.user
            flexural_bending_strength_model.published_date = timezone.now()
            flexural_bending_strength_model.save()
            return redirect(f'/flexural-bending-strength/detail/{pk}')
        return render(request, 'flexural_bending_strength/flexural_bending_strength_edit.html', {'form': form})
