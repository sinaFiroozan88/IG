from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views

urlpatterns = [
    path('new', views.Silis_New.as_view(), name='silis_new'),
    path('detail/<int:pk>', views.Silis_Detail.as_view(), name='silis_detail'),
    path('list', views.Silis_List.as_view(), name='silis_list'),
    path('delete/<int:pk>', views.Silis_Delete.as_view(), name='silis_delete'),
    path('edit/<int:pk>', views.Silis_Edit.as_view(), name='silis_edit'),
]
