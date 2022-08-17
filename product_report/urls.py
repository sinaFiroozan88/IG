from .views import ProductReport

from django.urls import path, include

urlpatterns = [
    path('product_report', ProductReport.as_view(), name='Product_Report_URL')
]
