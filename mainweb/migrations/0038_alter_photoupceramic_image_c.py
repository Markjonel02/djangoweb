# Generated by Django 4.1.4 on 2023-01-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0037_photoupceramic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoupceramic',
            name='Image_c',
            field=models.ImageField(blank=True, null=True, upload_to='ceramic_img'),
        ),
    ]
