from rest_framework import mixins, viewsets

from .models import Transaction, Wallet
from .serializers import TransactionSerializer, WalletSerializer

class WalletViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):

    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionViewSet(
    viewsets.ModelViewSet
        ):
    
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
