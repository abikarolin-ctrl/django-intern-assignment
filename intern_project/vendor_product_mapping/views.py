from django.http import JsonResponse
from .models import VendorProductMapping

def vendor_product_mapping_list(request):
    mappings = VendorProductMapping.objects.all().values()
    mapping_list = list(mappings)
    return JsonResponse(mapping_list, safe=False)