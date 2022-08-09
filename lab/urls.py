from django.urls import path
from . import views

urlpatterns = [
    path('', views.lab_list, name='lab_list'),
    path('<int:pk>/', views.lab_detail, name='lab_detail'),
    path('new/', views.lab_new, name='lab_new'),
    path('<int:pk>/edit/', views.lab_edit, name='lab_edit'),
    path('lab/<pk>/remove/', views.lab_remove, name='lab_remove'),
    path('ajax/load-quarters/', views.load_quarters, name='ajax_load_quarters' ),  # <-- this one here

]
