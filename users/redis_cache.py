import random
from django.core.cache import cache
from users.serializers import RedisCodeSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

class CreateRedisCode(APIView):
    def post(self, request):
        user = request.user

        code = str(random.randint(100000, 999999))

        if not user.is_authenticated:
            raise ValidationError("U must authorize to get a code")
        
        key = f"Code:{user.id}"
        cache.set(key, code, timeout=60)

        return Response("Code created open redis to see", status=200)
    
class CheckRedisCode(CreateAPIView):
    serializer_class = RedisCodeSerializer

    def post(self, request):
        user = request.user
        code = request.data.get("code")
          
        key = f"Code:{user.id}"  
        saved_code = cache.get(key)

        if not saved_code:
            return False
        
        if saved_code != code:
            return False
        
        cache.delete(user.id)
        
    
        return Response("code deleted", status=200)