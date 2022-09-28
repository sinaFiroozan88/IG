from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('new', views.QC_Retest_New.as_view(), name='quality_control_retest_new'),
    path('detail/<int:pk>', views.QC_Retest_Detail.as_view(), name='quality_control_retest_detail'),
    path('list', views.QC_Retest_List.as_view(), name='quality_control_retest_list'),
    path('edit/<int:pk>', views.QC_Retest_Edit.as_view(), name='quality_control_retest_edit'),
    path('delete/<int:pk>', views.QC_Retest_Delete.as_view(), name='quality_control_retest_delete'),
]