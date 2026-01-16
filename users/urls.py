from django.urls import path
from users.views import RegisterView, DeleteUsersView, ConfirmCodeView, UserAuthView, CustomJWTview
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenVerifyView
)
from users.google_oauth import GoogleLogin
from users.redis_cache import CreateRedisCode, CheckRedisCode

urlpatterns = [
    path("generate_code/", CreateRedisCode.as_view()),
    path("check_code/", CheckRedisCode.as_view()),
    path("register/", RegisterView.as_view()),
    path("<int:id>/", DeleteUsersView.as_view()),
    path("confirm/", ConfirmCodeView.as_view()),
    path("authenticate/", UserAuthView.as_view()),
    path('jwt/', CustomJWTview.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('google-login/', GoogleLogin.as_view())
]