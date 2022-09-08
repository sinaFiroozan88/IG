from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views

urlpatterns = [
    path('new', views.QualityControlView.as_view(), name='quality_control_nealit_new'),
    path('detail/<int:pk>', views.QC_Nealit_Detail.as_view(), name='quality_control_nealit_detail'),
    path('delete/<int:pk>', views.QC_Nealit_Delete.as_view(), name='quality_control_nealit_delete'),
    path('edit/<int:pk>', views.QC_Nealit_Edit.as_view(), name='quality_control_nealit_edit'),
    path('list', views.QC_Nealit_List.as_view(), name='quality_control_nealit_list'),
]
