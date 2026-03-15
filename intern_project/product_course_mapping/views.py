from django.http import JsonResponse
from .models import ProductCourseMapping

def product_course_mapping_list(request):
    mappings = ProductCourseMapping.objects.all().values()
    mapping_list = list(mappings)
    return JsonResponse(mapping_list, safe=False)