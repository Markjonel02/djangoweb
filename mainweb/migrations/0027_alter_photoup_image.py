# Generated by Django 4.1.4 on 2023-01-15 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0026_photoup_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoup',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='uploadedimg'),
        ),
    ]
