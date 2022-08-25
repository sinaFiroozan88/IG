from .views import ProductReport, ProductReportList, ProductReportDetail, ProductReportEdit, ProductReportDelete
from django.contrib.auth.decorators import login_required
from django.urls import path, include

urlpatterns = [
    path('product_report', ProductReport.as_view(), name='product_report'),
    path('product_report_list', ProductReportList, name='product_report_list'),
    path('product_report_detail/<int:pk>', ProductReportDetail, name='product_report_detail'),
    path('product_report/<int:pk>/edit', ProductReportEdit, name='product_report_edit'),
    path('product_report/<int:pk>/remove', ProductReportDelete, name='product_report_delete'),
]
