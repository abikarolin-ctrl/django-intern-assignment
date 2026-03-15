from django.urls import path
from .views import course_certification_mapping_list

urlpatterns = [
    path('', course_certification_mapping_list, name='course_certification_mapping_list'),
]