from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('new', views.Ten_Sieve_Analyse_New.as_view(), name='ten_sieve_analyse_new'),
    path('detail/<int:pk>', views.Ten_Sieve_Analyse_Detail.as_view(), name='ten_sieve_analyse_detail'),
    path('list', views.Ten_Sieve_Analyse_List.as_view(), name='ten_sieve_analyse_list'),
    path('delete/<int:pk>', views.Ten_Sieve_Analyse_Delete.as_view(), name='ten_sieve_analyse_delete'),
    path('edit/<int:pk>', views.Ten_Sieve_Analyse_Edit.as_view(), name='ten_sieve_analyse_edit'),
]
