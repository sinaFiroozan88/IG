from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('new', views.Blane_New.as_view(), name='blane_new'),
    path('detail/<int:pk>', views.Blane_Detail.as_view(), name='blane_detail'),
    path('list', views.Blane_List.as_view(), name='blane_list'),
    path('delete/<int:pk>', views.Blane_Delete.as_view(), name='blane_delete'),
    path('edit/<int:pk>', views.Blane_Edit.as_view(), name='blane_edit'),
]