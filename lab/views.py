from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from general.models import Quarter
from .models import Lab
from .forms import LabForm
# Create your views here.
# from jalali_date import datetime2jalali, date2jalali

# @login_required
# def my_view(request):
#     jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')


@login_required
def lab_list(request):
    labs = Lab.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'lab/lab_list1.html', {'labs': labs})


@login_required
def lab_detail(request, pk):

    lab = get_object_or_404(Lab, pk=pk)
    return render(request, 'lab/lab_detail1.html', {'lab': lab})

# def lab_new(request):
#     form = LabForm()
#     return render(request, 'lab/lab_edit.html', {'form': form})


@login_required
def lab_new(request):
    if request.method == "POST":
        form = LabForm(request.POST)
        if form.is_valid():
            lab = form.save(commit=False)
            lab.author = request.user
            lab.published_date = timezone.now()
            lab.save()
            return redirect('lab_detail', pk=lab.pk)
    else:
        form = LabForm()
    return render(request, 'lab/lab_edit1.html', {'form': form})


@login_required
def lab_remove(request, pk):
    lab = get_object_or_404(Lab, pk=pk)
    lab.delete()
    return redirect(reverse('lab_list'))


# def lab_new(request):
#     if request.method == "POST":
#          form = LabForm(request.POST)
#           if form.is_valid():
#             lab = form.save( commit=False )
#             lab.author = request.user
#             lab.published_date = timezone.now()
#             lab.save()
#             return redirect('lab/lab_detail', pk=lab.pk )
#           else:
#         form = LabForm()
#     return render(request, 'lab/lab_detail.html', {'form':form})


@login_required
def lab_edit(request, pk):
    lab = get_object_or_404(Lab, pk=pk)
    if request.method == "POST":
        form = LabForm(request.POST, instance=lab)
        if form.is_valid():
            # if request.user.is_superuser():
            lab = form.save(commit=False)
            lab.author = request.user
            lab.published_date = timezone.now()
            lab.save()
            return redirect('lab_detail', pk=lab.pk)
    else:
        form = LabForm(instance=lab)
    return render(request, 'lab/lab_edit1.html', {'form': form})


def load_quarters(request):
    hour_id = request.GET.get('hour')
    quarters = Quarter.objects.filter(hour_id=hour_id).order_by('quarter')
    return render(request, 'lab/quarter_dropdown_list_options.html', {'quarters': quarters})