from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from . import models
from .forms import Blane_Form
from django.views import View
from . import forms


class Blane_New(View):
    def get(self, request):
        form = forms.Blane_Form()
        return render(request, 'blane/blane_new.html', {
            'form': form
        })

    def post(self, request):
        form = forms.Blane_Form(request.POST)
        if form.is_valid():
            blane = form.save(commit=False)
            blane.author = request.user
            blane.published_date = timezone.now()
            form.save()
            return redirect('blane_detail', pk=blane.pk)

        return render(request, 'blane/blane_new.html', {
            'form': form
        })

class Blane_Detail(View):
    def get(self, request, pk):
        blane_detail = get_object_or_404(models.Blane_Model, pk=pk)
        context = {
            'detail': blane_detail
        }
        return render(request, 'blane/blane_detail.html', context)

    def post(self, request, pk):
        blane_detail = get_object_or_404(models.Blane_Model, pk=pk)
        context = {
            'detail': blane_detail
        }
        return render(request, 'blane/blane_detail.html', context)


class Blane_List(View):
    def get(self, request):
        blane_list = models.Blane_Model.objects.all().order_by('published_date')
        context = {
            'lists': blane_list
        }
        return render(request, 'blane/blane_list.html', context)

    def post(self, request):
        blane_list = models.Blane_Model.objects.all().order_by('published_date')
        context = {
            'lists': blane_list
        }
        return render(request, 'blane/blane_list.html', context)


class Blane_Delete(View):
    def get(self, request, pk):
        blane_model = get_object_or_404(models.Blane_Model, pk=pk)
        blane_model.delete()
        return redirect(reverse('blane_new'))

    def post(self, request, pk):
        blane_model = get_object_or_404(models.Blane_Model, pk=pk)
        blane_model.delete()
        return redirect(reverse('blane_new'))


class Blane_Edit(View):
    def get(self, request, pk):
        blane_model = get_object_or_404(models.Blane_Model, pk=pk)
        form = Blane_Form(instance=blane_model)
        return render(request, 'blane/blane_edit.html', {'form': form})

    def post(self, request, pk):
        blane_model = get_object_or_404(models.Blane_Model, pk=pk)
        form = Blane_Form(request.POST, instance=blane_model)
        if form.is_valid():
            blane_model = form.save(commit=False)
            blane_model.author = request.user
            blane_model.published_date = timezone.now()
            blane_model.save()
            return redirect(f'/blane/detail/{pk}')
        return render(request, 'blane/blane_edit.html', {'form': form})
