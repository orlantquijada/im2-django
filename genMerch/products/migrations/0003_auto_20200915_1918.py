# Generated by Django 3.1.1 on 2020-09-15 11:18

from django.db import migrations
import genMerch.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200915_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=genMerch.fields.TitleCaseCharfield(max_length=40),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=genMerch.fields.TitleCaseCharfield(max_length=40),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=genMerch.fields.TitleCaseCharfield(max_length=40),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_name',
            field=genMerch.fields.TitleCaseCharfield(max_length=40),
        ),
    ]
