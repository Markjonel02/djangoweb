# Generated by Django 4.1.4 on 2023-01-15 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0029_alter_photoup_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoup',
            name='Updload_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
