# Generated by Django 4.1.4 on 2023-01-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0023_photoup_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoup',
            name='Category',
            field=models.CharField(max_length=50, null=True),
        ),
    ]