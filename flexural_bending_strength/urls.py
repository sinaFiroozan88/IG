from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('new', views.Flexural_Bending_Strength_New.as_view(), name='flexural_bending_strength_new'),
    path('detail/<int:pk>', views.Flexural_Bending_Strength_Detail.as_view(), name='flexural_bending_strength_detail'),
    path('list', views.Flexural_Bending_Strength_List.as_view(), name='flexural_bending_strength_list'),
    path('edit/<int:pk>', views.Flexural_Bending_Strength_Edit.as_view(), name='flexural_bending_strength_edit'),
    path('delete/<int:pk>', views.Flexural_Bending_Strength_Delete.as_view(), name='flexural_bending_strength_delete')
]