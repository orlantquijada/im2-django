# Generated by Django 3.1.1 on 2020-09-24 18:38

from django.db import migrations
import genMerch.fields


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20200924_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='father_occupation',
            field=genMerch.fields.TitleCaseCharfield(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='middle_name',
            field=genMerch.fields.TitleCaseCharfield(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='mother_occupation',
            field=genMerch.fields.TitleCaseCharfield(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='religion',
            field=genMerch.fields.TitleCaseCharfield(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='spouse_name',
            field=genMerch.fields.TitleCaseCharfield(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='spouse_occupation',
            field=genMerch.fields.TitleCaseCharfield(blank=True, default='', max_length=40, null=True),
        ),
    ]
