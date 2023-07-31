from django.core.validators import EmailValidator
from rest_framework import serializers
from .models import Customer

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailValidator()])

    class Meta:
        model = Customer
        fields = ['id','name', 'password', 'email', 'phone', 'city']
        extra_kwargs = {
            'password': {'write_only': True},
        }

        
