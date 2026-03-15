from django.http import JsonResponse
from .models import Course

def course_list(request):
    courses = Course.objects.all().values()
    course_list = list(courses)
    return JsonResponse(course_list, safe=False)