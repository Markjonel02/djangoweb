# Generated by Django 4.1.4 on 2023-01-29 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0047_myuser_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='password',
        ),
    ]