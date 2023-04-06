from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import View
from .forms import Avg_Test_Production_Form
from . import models


class Avg_Test_Production_New(View):
    def get(self, request):
        form = Avg_Test_Production_Form()
        return render(request, 'avg_test_production/avg_test_production_new.html', {
            'form': form
        })

    def post(self, request):
        form = Avg_Test_Production_Form(request.POST)
        if form.is_valid():
            avg_test_production_new = form.save(commit=False)
            avg_test_production_new.author = request.user
            avg_test_production_new.published_date = timezone.now()
            form.save()
            # return redirect('product_detail', pk=product.pk)
            return redirect('home_page')
        return render(request, 'avg_test_production/avg_test_production_new.html', {'form': form})


class Avg_Test_Production_Detail(View):
    def get(self, request, pk):
        avg_test_production_detail = get_object_or_404(models.Avg_Test_Production_Model, pk=pk)
        context = {
            'detail': avg_test_production_detail
        }
        return render(request, 'avg_test_production/avg_test_production_detail.html', context)

    def post(self, request, pk):
        avg_test_production_detail = get_object_or_404(models.Avg_Test_Production_Model, pk=pk)
        context = {
            'detail': avg_test_production_detail
        }
        return render(request, 'avg_test_production/avg_test_production_detail.html', context)


class Avg_Test_Production_List(View):
    def get(self, request):
        avg_test_production_list = models.Avg_Test_Production_Model.objects.all().order_by('published_date')
        context = {
            'lists': avg_test_production_list
        }
        return render(request, 'avg_test_production/avg_test_production_list.html', context)

    def post(self, request):
        avg_test_production_list = models.Avg_Test_Production_Model.objects.all().order_by('published_date')
        context = {
            'lists': avg_test_production_list
        }
        return render(request, 'avg_Test_production/avg_test_production_list.html', context)


class Avg_Test_Production_Delete(View):
    def get(self, request, pk):
        avg_test_production_model = get_object_or_404(models.Avg_Test_Production_Model, pk=pk)
        avg_test_production_model.delete()
        return redirect(reverse('avg_test_production_list'))

    def post(self, request, pk):
        avg_test_production_model = get_object_or_404(models.Avg_Test_Production_Model, pk=pk)
        avg_test_production_model.delete()
        return redirect(reverse('avg_test_production_list'))


class Avg_Test_Production_Edit(View):
    def get(self, request, pk):
        avg_test_production_model = get_object_or_404(models.Avg_Test_Production_Model, pk=pk)
        form = Avg_Test_Production_Form(instance=avg_test_production_model)
        return render(request, 'avg_test_production/avg_Test_production_edit.html', {'form': form})

    def post(self, request, pk):
        avg_test_production_model = get_object_or_404(models.Avg_Test_Production_Model, pk=pk)
        form = Avg_Test_Production_Form(request.POST, instance=avg_test_production_model)
        if form.is_valid():
            avg_test_production_model = form.save(commit=False)
            avg_test_production_model.author = request.user
            avg_test_production_model.Published_Date = timezone.now()
            avg_test_production_model.save()
            return redirect(f'/avg-test-production/detail/{pk}')
        return render(request, 'avg_test_production/avg_Test_production_edit.html', {'form': form})
