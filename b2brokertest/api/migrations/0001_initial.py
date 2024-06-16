# Generated by Django 5.0.6 on 2024-06-16 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=30)),
                ('balance', models.DecimalField(decimal_places=18, max_digits=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txid', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=18, max_digits=30)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.wallet')),
            ],
        ),
    ]
