# Generated by Django 5.1.2 on 2024-11-12 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrecords',
            name='fee_payment_status',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentrecords',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentrecords',
            name='reg_no',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='studentrecords',
            name='reporting_status',
            field=models.CharField(max_length=100),
        ),
    ]
