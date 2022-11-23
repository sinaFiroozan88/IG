from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('new', views.Block_Water_Acid_New.as_view(), name='block_water_acid_new'),
    path('detail/<int:pk>', views.Block_Water_Acid_Detail.as_view(), name='block_water_acid_detail'),
    path('list', views.Block_Water_Acid_List.as_view(), name='block_water_acid_list'),
    path('delete/<int:pk>', views.Block_Water_Acid_Delete.as_view(), name='block_water_acid_delete'),
    path('edit/<int:pk>', views.Block_Water_Acid_Edit.as_view(), name='block_water_acid_edit'),
]