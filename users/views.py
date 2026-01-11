from rest_framework.response import Response
from users.serializers import (UserAuthSerializer,
                                RegisterSerializer,
                                Confirmation,
                                CustomJWTSerializer)
from users.models import Confirm
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.exceptions import ValidationError
from users.models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.
class CustomJWTview(TokenObtainPairView):
    serializer_class = CustomJWTSerializer

class RegisterView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

class UserAuthView(CreateAPIView):
    serializer_class = UserAuthSerializer
    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class ConfirmCodeView(CreateAPIView):
    serializer_class = Confirmation
    def post(self, request):
        serializer = Confirmation(data=request.data)    
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data["code"]
        user = serializer.validated_data["user_id"]

        try:
            confirm = Confirm.objects.get(code=code)
        except Confirm.DoesNotExist:
            raise ValidationError("Invalid code or user")
        
        user = confirm.user
        user.is_active = True
        user.save()

        return Response(data={"user confirmed"})

class DeleteUsersView(DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    lookup_field = "id"