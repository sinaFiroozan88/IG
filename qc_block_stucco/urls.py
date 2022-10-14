from django.contrib import admin
# from django.contrib.auth import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import QC_Block_Stucco_New, QC_Block_Stucco_Detail, QC_Block_Stucco_List, QC_Block_Stucco_Delete, QC_Block_Stucco_Edit


urlpatterns = [
    path('new', QC_Block_Stucco_New.as_view(), name='qc_block_stucco_new'),
    path('detail/<int:pk>', QC_Block_Stucco_Detail.as_view(), name='qc_block_stucco_detail'),
    path('list', QC_Block_Stucco_List.as_view(), name='qc_block_stucco_list'),
    path('delete/<int:pk>', QC_Block_Stucco_Delete.as_view(), name='qc_block_stucco_delete'),
    path('edit/<int:pk>', QC_Block_Stucco_Edit.as_view(), name='qc_block_stucco_edit'),
]
