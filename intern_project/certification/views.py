from django.http import JsonResponse
from .models import Certification

def certification_list(request):
    certifications = Certification.objects.all().values()
    certification_list = list(certifications)
    return JsonResponse(certification_list, safe=False)