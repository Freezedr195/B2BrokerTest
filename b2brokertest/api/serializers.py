from rest_framework import serializers

from .models import Transaction, Wallet


class WalletSerializer(serializers.ModelSerializer):

    # Balance could be changed only through transaction
    balance = serializers.CharField(read_only=True)

    class Meta:
        model = Wallet
        fields = "__all__"


class TransactionReadOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ("id", "amount", "txid", "wallet")


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = "__all__"
