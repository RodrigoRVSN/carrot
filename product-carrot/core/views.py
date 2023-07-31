from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import ProductSerializer
from .models import Product

class ProductView(APIView):
    # TODO: fix authentication middleware
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        products = Product.objects.all() 

        if len(products) == 0:
            return Response(status = status.HTTP_204_NO_CONTENT)
        
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        name = request.data.get("name")
        price = request.data.get("price")
        available = request.data.get("available", True)

        if not name or not price:
            return Response({"error": "a field is missing."}, status = status.HTTP_400_BAD_REQUEST)
        
        product = Product(name=name, price=price, available=available)
        product.save()

        return Response({"message": "product created successfully!"}, status = status.HTTP_201_CREATED)
    