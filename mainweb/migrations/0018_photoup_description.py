# Generated by Django 4.1.4 on 2023-01-15 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0017_photoup'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoup',
            name='Description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
