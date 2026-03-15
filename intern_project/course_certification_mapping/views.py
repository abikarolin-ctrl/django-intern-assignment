from django.http import JsonResponse
from .models import CourseCertificationMapping

def course_certification_mapping_list(request):
    mappings = CourseCertificationMapping.objects.all().values()
    mapping_list = list(mappings)
    return JsonResponse(mapping_list, safe=False)