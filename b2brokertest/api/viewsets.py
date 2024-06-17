from rest_framework import mixins, viewsets

from .models import Transaction, Wallet
from .serializers import (
    TransactionReadOnlySerializer,
    TransactionSerializer,
    WalletSerializer,
)


class WalletViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return TransactionReadOnlySerializer
        return super().get_serializer_class()
