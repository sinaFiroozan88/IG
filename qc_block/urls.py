from django.contrib import admin
# from django.contrib.auth import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import QC_Block_New, QC_Block_Detail, QC_Block_List, QC_Blcok_Delete, QC_Block_Edit


urlpatterns = [
    path('new', QC_Block_New.as_view(), name='qc_block_new'),
    path('detail/<int:pk>', QC_Block_Detail.as_view(), name='qc_block_detail'),
    path('list', QC_Block_List.as_view(), name='qc_block_list'),
    path('delete/<int:pk>', QC_Blcok_Delete.as_view(), name='qc_block_delete'),
    path('edit/<int:pk>', QC_Block_Edit.as_view(), name='qc_block_edit'),
]
