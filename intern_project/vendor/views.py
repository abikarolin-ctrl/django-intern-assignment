from django.http import JsonResponse
from .models import Vendor

def vendor_list(request):
    vendors = Vendor.objects.all().values()
    vendor_list = list(vendors)
    return JsonResponse(vendor_list, safe=False)