from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.bascule, name='bascule'),
]