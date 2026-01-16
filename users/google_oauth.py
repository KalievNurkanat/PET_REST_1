import requests
from users.serializers import OauthAPISerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
import os

User = get_user_model()

class GoogleLogin(CreateAPIView):
    serializer_class = OauthAPISerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data["code"]

        token_response = requests.post(
            url="https://oauth2.googleapis.com/token",
            data={
                "code": code,
                "client_id": os.environ.get("CLIENT_ID"),
                "client_secret": os.environ.get("CLIENT_SECRET"),
                "redirect_uri": os.environ.get("REDIRECT_URI"),
                "grant_type": "authorization_code"
            }
        )
        
        token_data = token_response.json()
        access_token = token_data.get("access_token")

        if not access_token:
            return Response("Invalid access token")
        
        user_info = requests.get(
            url="https://www.googleapis.com/oauth2/v3/userinfo",
            params={"alt":"json"},
            headers={"Authorization": f"Bearer {access_token}"}
        ).json()


        email = user_info.get("email")
        first_name = user_info.get("given_name", "")
        last_name = user_info.get("family_name", "")

        user, created = User.objects.get_or_create(
            email=email, first_name=first_name, last_name=last_name, is_active=True
        )

        refresh_token = RefreshToken.for_user(user)
        refresh_token["email"] = user.email


        return Response({"access_token": str(refresh_token.access_token),
                         "refresh_token": str(refresh_token)})





