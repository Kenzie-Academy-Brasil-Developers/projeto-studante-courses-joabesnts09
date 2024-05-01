from rest_framework import generics
from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer