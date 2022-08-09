from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.hse, name='hse'),
]