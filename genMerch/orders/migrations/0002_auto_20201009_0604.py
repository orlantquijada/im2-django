# Generated by Django 3.1.1 on 2020-10-08 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='quantity',
        ),
    ]
