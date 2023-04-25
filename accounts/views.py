from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import AccountRegisterSerializer


User = get_user_model()


class AccountRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = AccountRegisterSerializer