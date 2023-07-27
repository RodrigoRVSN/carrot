from django.http import JsonResponse
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ProductSerializer

@api_view(['GET'])
def get_all_products(request):
    products = Product.objects.all() 
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)
