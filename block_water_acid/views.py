from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from . import models
from .forms import Block_Water_Acid_Form
from django.views import View
from . import forms


class Block_Water_Acid_New(View):
    def get(self, request):
        form = forms.Block_Water_Acid_Form()
        return render(request, 'block_water_acid/block_water_acid_new.html', {
            'form': form
        })

    def post(self, request):
        form = forms.Block_Water_Acid_Form(request.POST)
        if form.is_valid():
            block_water_acid = form.save(commit=False)
            block_water_acid.author = request.user
            block_water_acid.published_date = timezone.now()
            form.save()
            return redirect('block_water_acid_detail', pk=block_water_acid.pk)
            # return redirect('home_page')

        return render(request, 'block_water_acid/block_water_acid_detail.html', {
            'form': form
        })

class Block_Water_Acid_Detail(View):
    def get(self, request, pk):
        block_water_acid_detail = get_object_or_404(models.Block_Water_Acid_Model, pk=pk)
        context = {
            'detail': block_water_acid_detail
        }
        return render(request, 'block_water_acid/block_water_acid_detail.html', context)

    def post(self, request, pk):
        block_water_acid_detail = get_object_or_404(models.Block_Water_Acid_Model, pk=pk)
        context = {
            'detail': block_water_acid_detail
        }
        return render(request, 'blane/blane_detail.html', context)


class Block_Water_Acid_List(View):
    def get(self, request):
        block_water_acid_list = models.Block_Water_Acid_Model.objects.all().order_by('published_date')
        context = {
            'lists': block_water_acid_list
        }
        return render(request, 'block_water_acid/block_water_acid_list.html', context)

    def post(self, request):
        block_water_acid_list = models.Block_Water_Acid_Model.objects.all().order_by('published_date')
        context = {
            'lists': block_water_acid_list
        }
        return render(request, 'block_water_acid/block_water_acid_list.html', context)


class Block_Water_Acid_Delete(View):
    def get(self, request, pk):
        blane_model = get_object_or_404(models.Block_Water_Acid_Model, pk=pk)
        blane_model.delete()
        return redirect(reverse('block_water_acid_new'))

    def post(self, request, pk):
        blane_model = get_object_or_404(models.Block_Water_Acid_Model, pk=pk)
        blane_model.delete()
        return redirect(reverse('block_water_acid_new'))


class Block_Water_Acid_Edit(View):
    def get(self, request, pk):
        block_water_acid_model = get_object_or_404(models.Block_Water_Acid_Model, pk=pk)
        form = Block_Water_Acid_Form(instance=block_water_acid_model)
        return render(request, 'block_water_acid/block_water_acid_edit.html', {'form': form})

    def post(self, request, pk):
        block_water_acid_model = get_object_or_404(models.Block_Water_Acid_Model, pk=pk)
        form = Block_Water_Acid_Form(request.POST, instance=block_water_acid_model)
        if form.is_valid():
            block_water_acid_model = form.save(commit=False)
            block_water_acid_model.author = request.user
            block_water_acid_model.published_date = timezone.now()
            block_water_acid_model.save()
            return redirect(f'/block-water-acid/detail/{pk}')
        return render(request, 'block_water_acid/block_water_acid_edit.html', {'form': form})
