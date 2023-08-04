from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import  AccessToken
from .serializer import UserSerializer
from .models import Customer
from .jwt import CustomJWTAuthentication

class UserRegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    authentication_classes = [CustomJWTAuthentication]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        if user.check_password(password):
            access_token = AccessToken.for_user(user = user)
            token = str(access_token)
            return Response({'access_token': token}, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)




