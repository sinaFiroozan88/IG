from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.canteen_list, name='canteen'),
    path('<int:pk>/', views.canteen_detail, name='canteen_detail'),
    path('new/', views.canteen_new, name='canteen_new'),
    path('<int:pk>/edit/', views.canteen_edit, name='canteen_edit'),
    path('ajax/load-food-fields/', views.load_food_fields, name='ajax_load_food_fields'),

]
