from .views import Avg_Test_Production_New, Avg_Test_Production_Detail, Avg_Test_Production_List, Avg_Test_Production_Delete, Avg_Test_Production_Edit
from django.contrib.auth.decorators import login_required
from django.urls import path, include

urlpatterns = [
    path('new', Avg_Test_Production_New.as_view(), name='avg_test_product ion_new'),
    path('detail/<int:pk>', Avg_Test_Production_Detail.as_view(), name='avg_test_production_detail'),
    path('list', Avg_Test_Production_List.as_view(), name='avg_test_production_list'),
    path('edit/<int:pk>', Avg_Test_Production_Edit.as_view(), name='avg_test_production_edit'),
    path('delete/<int:pk>', Avg_Test_Production_Delete.as_view(), name='avg_test_production_delete'),
]
