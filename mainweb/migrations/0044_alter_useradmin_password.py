# Generated by Django 4.1.4 on 2023-01-27 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0043_alter_photoup_image_alter_photoupceramic_image_c_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useradmin',
            name='Password',
            field=models.CharField(choices=[('admin', 'Admin'), ('staff', 'Staff')], max_length=50),
        ),
    ]
