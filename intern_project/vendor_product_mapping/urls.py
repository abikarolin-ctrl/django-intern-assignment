from django.urls import path
from .views import vendor_product_mapping_list

urlpatterns = [
    path('', vendor_product_mapping_list, name='vendor_product_mapping_list'),
]