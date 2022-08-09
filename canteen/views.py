from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Food, Ingredient, DailyMeal
from .forms import DailyMealForm


# Create your views here.
def canteen_list(request):
    dailymeals = DailyMeal.objects.all()
    return render(request, 'canteen/canteen_list.html', {'dailymeals': dailymeals})


def canteen_detail(request, pk):
    dailymeal = get_object_or_404(DailyMeal, pk= pk)
    return render(request, 'canteen/canteen_detail.html', {'dailymeal':dailymeal})


@login_required
def canteen_new(request):
    if request.method == "POST":
        form = DailyMealForm(request.POST)
        if form.is_valid():
            lab = form.save(commit=False)
            lab.author = request.user
            lab.published_date = timezone.now()
            lab.save()
            return redirect('canteen_detail', pk=lab.pk)
    else:
        form = DailyMealForm()
    return render(request, 'canteen/canteen_edit1.html', {'form': form})


def canteen_edit(request, pk):

    pass


def load_food_fields(request):
    form = DailyMealForm()
    food_id = request.GET.get('food')
    f = Ingredient.objects.filter(pk=food_id)
    food_fields = []
    print(f[2])
    return render(request, 'lab/quarter_dropdown_list_options.html', {'form': form})
