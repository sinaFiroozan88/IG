from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
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
        form = BlockForm()
        context = {
            "form": form
        }
        return render(request, 'block/block.html', context)

    def post(self, request):
        form = BlockForm(request.POST)
        if form.is_valid():
            block_item = form.save(commit=False)
            block_item.author = request.user
            block_item.published_date = timezone.now()
            block_item.save()
        context = {
            "form": form
        }
        return render(request, 'block/block.html', context)
