from django.shortcuts import render


# Create your views here.
from block.forms import BlockForm
from blog.forms import PostForm


def block(request):
    form = BlockForm
    context = {
        "form": form
    }
    print(context)
    return render(request, 'block/block.html', context)
