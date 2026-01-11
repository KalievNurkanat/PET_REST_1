from django.urls import path
from users.views import RegisterView, DeleteUsersView, ConfirmCodeView, UserAuthView, CustomJWTview
from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenVerifyView
)

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("<int:id>/", DeleteUsersView.as_view()),
    path("confirm/", ConfirmCodeView.as_view()),
    path("authenticate/", UserAuthView.as_view()),
    path('jwt/', CustomJWTview.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify')
]