from django.db import models


# Create your models here.
class Wallet(models.Model):
    """Wallet model."""

    label = models.CharField(max_length=30)
    balance = models.DecimalField(decimal_places=18, max_digits=30, default="0.00")


class Transaction(models.Model):
    """Transaction model."""

    txid = models.CharField(max_length=30)
    amount = models.DecimalField(decimal_places=18, max_digits=30)
    wallet = models.ForeignKey(to=Wallet, on_delete=models.PROTECT)
