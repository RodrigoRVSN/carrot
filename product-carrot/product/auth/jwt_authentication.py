from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import Customer

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        try:
            user_id = validated_token['user_id']
            user = Customer.objects.get(id=user_id)
            return user
        except Customer.DoesNotExist:
            return None