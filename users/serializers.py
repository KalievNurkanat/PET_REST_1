from rest_framework import serializers
import random
from users.models import CustomUser
from users.models import Confirm
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class OauthAPISerializer(serializers.Serializer):
    code = serializers.CharField()

class RedisCodeSerializer(serializers.Serializer):
    code = serializers.CharField()

class CustomJWTSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = str(user.email)

        return token

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = CustomUser
        fields = ["id", "username", "password", "phone_number", "email"]

    
    def validate_username(self, username):
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError({"Error": "such a user exists"})
        return username
    
    def create(self, validated_data):
        password = validated_data.pop("password")

        user = CustomUser.objects.create_user(username=validated_data["username"],
                                              phone_number=validated_data["phone_number"],
                                   password = password, is_active=False,
                                   email=validated_data["email"])
        
        user.save()

        code = str(random.randint(100000, 999999))
        Confirm.objects.create(code=code, user=user)
        return user


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=35)
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(
            username=data["username"],
            password=data["password"]
        )

        if user is None:
            raise serializers.ValidationError("Неверный логин или пароль")

        if not user.is_active:
            raise serializers.ValidationError("Аккаунт не активирован")

        data["user"] = user
        return data
        
class Confirmation(serializers.Serializer):
    code = serializers.CharField(max_length=6)
    user_id = serializers.IntegerField()
