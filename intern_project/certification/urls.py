from django.urls import path
from .views import certification_list

urlpatterns = [
    path('', certification_list, name='certification_list'),
]