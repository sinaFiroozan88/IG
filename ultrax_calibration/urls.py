from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('new', views.Ultrax_New.as_view(), name='ultrax_calibration_new'),
    path('detail/<int:pk>', views.Ultrax_Detail.as_view(), name='ultrax_calibration_detail'),
    path('list', views.Ultrax_List.as_view(), name='ultrax_calibration_list'),
    path('delete/<int:pk>', views.Ultrax_Delete.as_view(), name='ultrax_calibration_delete'),
    path('edit/<int:pk>', views.Ultrax_Edit.as_view(), name='ultrax_calibration_edit'),
]
