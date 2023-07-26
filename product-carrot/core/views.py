from django.http import JsonResponse

def get_all_receipts(request):
    data = {"message": "ok"}
    return JsonResponse(data)
