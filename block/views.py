from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.utils import timezone
from django.views import View

from .forms import BlockForm
from .models import Block


# @login_required
# def block(request):
#     if request.method == "POST":
#         form = BlockForm(request.POST)
#         if form.is_valid():
#             block_item = form.save(commit=False)
#             block_item.author = request.user
#             block_item.published_date = timezone.now()
#             block_item.save()
#     else:
#         form = BlockForm()
#     context = {
#         "form": form
#     }
#     return render(request, 'block/block.html', context)

class BlockView(View):
    def get(self, request):
        form = BlockForm
        context = {
            "form": form
        }
        return render(request, 'block/block.html', context)

    def post(self, request):
        form = BlockForm(request.POST)
        context = {
            "form": form
        }
        # block_item = form.save(commit=False)
        form.author = request.user
        form.published_date = timezone.now()
        if form.is_valid():

            form.save()
            return redirect(reverse('home_page'))
        else:
            return redirect(reverse('Product_Report_URL'))

