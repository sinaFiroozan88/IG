from django.urls import path, include
from .views import Product, ProductList, ProductDetail, ProductRemove, ProductEdit

urlpatterns =[
    path('new', Product.as_view(), name='product_new'),
    path('list', ProductList.as_view(), name='product_list'),
    path('detail/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('remove/<int:pk>', ProductRemove.as_view(), name='product_remove'),
    path('edit/<int:pk>', ProductEdit.as_view(), name='product_edit'),
]