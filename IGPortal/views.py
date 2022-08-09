import itertools
from django.shortcuts import render
from django.utils import timezone
from slider.models import Slider
from blog.models import Post
from site_setting.models import SiteSetting


# header code behind
def header(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'shared/header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'shared/footer.html', context)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


# code behind
def home_page(request):
    sliders = Slider.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]
    context = {
        'data': 'این پورتال درون سازماتی با فریم ورک django نوشته شده',
        'sliders': sliders,
        'posts': posts,
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'about_page.html', context)
