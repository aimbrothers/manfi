from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import AccountRegisterView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login_user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', AccountRegisterView.as_view(), name='register_user'),
]