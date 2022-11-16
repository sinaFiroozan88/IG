from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import View
from .forms import Silis_Form
from . import models


class Silis_New(View):
    def get(self, request):
        form = Silis_Form()
        return render(request, 'silis/silis_new.html', {
            'form': form
        })

    def post(self, request):
        form = Silis_Form(request.POST)
        if form.is_valid():
            silis_form = form.save(commit=False)
            silis_form.author = request.user
            silis_form.published_date = timezone.now()
            form.save()
            # return redirect('quality_control_nealit_detail', pk=silis_form.pk)
            return redirect('home_page')
        return render(request, 'silis/silis_new.html', {'form': form})


class Silis_Detail(View):
    def get(self, request, pk):
        silis = get_object_or_404(models.Silis_Model, pk=pk)
        context = {
            'detail': silis
        }
        return render(request, 'silis/silis_detail.html', context)

    def post(self, request, pk):
        silis = get_object_or_404(models.Silis_Model, pk=pk)
        context = {
            'detail': silis
        }
        return render(request, 'silis/silis_detail.html', context)



class Silis_List(View):
    def get(self, request):
        silis_list = models.Silis_Model.objects.all().order_by('published_date')
        context = {
            'lists': silis_list
        }
        return render(request, 'silis/silis_list.html', context)

    def post(self, request):
        silis_list = models.Silis_Model.objects.all().order_by('published_date')
        context = {
            'lists': silis_list
        }
        return render(request, 'silis/silis_list.html', context)

class Silis_Delete(View):
    def get(self, request, pk):
        product = get_object_or_404(models.Silis_Model, pk=pk)
        product.delete()
        return redirect(reverse('silis_new'))

    def post(self, request, pk):
        product = get_object_or_404(models.Silis_Model, pk=pk)
        product.delete()
        return redirect(reverse('silis_new'))


class Silis_Edit(View):
    def get(self, request, pk):
        silis_model = get_object_or_404(models.Silis_Model, pk=pk)
        form = Silis_Form(instance=silis_model)
        return render(request, 'silis/silis_edit.html', {'form': form})

    def post(self, request, pk):
        silis_model = get_object_or_404(models.Silis_Model, pk=pk)
        form = Silis_Form(request.POST, instance=silis_model)
        if form.is_valid():
            silis_model = form.save(commit=False)
            silis_model.author = request.user
            silis_model.published_date = timezone.now()
            silis_model.save()
            return redirect(f'/silis/detail/{pk}')
        return render(request, 'silis/silis_edit.html', {'form': form})
