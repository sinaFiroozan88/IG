from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BlockView.as_view(), name='block'),
]
