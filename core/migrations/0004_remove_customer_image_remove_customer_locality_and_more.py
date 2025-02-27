# Generated by Django 5.0.3 on 2024-03-29 06:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='image',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, default=False, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.cart'),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, default=False, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, default=False, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, default=False, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.IntegerField(blank=True, default=False, null=True),
        ),
    ]
