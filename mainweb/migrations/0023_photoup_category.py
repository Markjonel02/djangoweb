# Generated by Django 4.1.4 on 2023-01-15 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0022_remove_photoup_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoup',
            name='Category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
