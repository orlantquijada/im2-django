# Generated by Django 3.1.1 on 2020-10-10 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20201010_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]