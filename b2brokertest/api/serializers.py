from rest_framework.serializers import ModelSerializer

from .models import Transaction, Wallet


class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
