# Generated by Django 5.0.3 on 2024-04-01 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_orderproduct_amount_orderproduct_total_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='paymnet_type',
            new_name='payment_type',
        ),
    ]
