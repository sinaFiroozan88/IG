from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import View
from .forms import Product_Form
from . import models


class Product(View):
    def get(self, request):
        form = Product_Form()
        return render(request, 'product/product_new.html', {
            'form': form
        })

    def post(self, request):
        form = Product_Form(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.published_date = timezone.now()
            form.save()
            return redirect('product_detail', pk=product.pk)
        return render(request, 'product/product_new.html', {'form': form})


class ProductList(View):
    def get(self, request):
        product_list = models.ProductModel.objects.all().order_by('published_date')
        context = {
            'lists': product_list
        }
        return render(request, 'product/product_list.html', context)

    def post(self, request):
        product_list = models.ProductModel.objects.all().order_by('published_date')
        context = {
            'lists': product_list
        }
        return render(request, 'product/product_list.html', context)


class ProductDetail(View):
    def get(self, request, pk):
        product_detail = get_object_or_404(models.ProductModel, pk=pk)
        context = {
            'detail': product_detail
        }
        return render(request, 'product/product_detail.html', context)

    def post(self, request, pk):
        product_detail = get_object_or_404(models.ProductModel, pk=pk)
        context = {
            'detail': product_detail
        }
        return render(request, 'product/product_detail.html', context)


class ProductRemove(View):
    def get(self, request, pk):
        product = get_object_or_404(models.ProductModel, pk=pk)
        product.delete()
        return redirect(reverse('product_list'))

    def post(self, request, pk):
        product = get_object_or_404(models.ProductModel, pk=pk)
        product.delete()
        return redirect(reverse('product_list'))


class ProductEdit(View):
    def get(self, request, pk):

        product_model = get_object_or_404(models.ProductModel, pk=pk)
        form = Product_Form(instance=product_model)
        return render(request, 'product/product_edit.html', {'form': form})

    def post(self, request, pk):
        product_model = get_object_or_404(models.ProductModel, pk=pk)
        form = Product_Form(request.POST, instance=product_model)
        if form.is_valid():
            product_model = form.save(commit=False)
            product_model.author = request.user
            product_model.Published_Date = timezone.now()
            product_model.save()
            return redirect(f'/product/detail/{pk}')
        return render(request, 'product/product_edit.html', {'form': form})
