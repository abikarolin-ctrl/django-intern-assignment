from django.urls import path
from .views import product_course_mapping_list

urlpatterns = [
    path('', product_course_mapping_list),
]