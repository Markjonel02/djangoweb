# Generated by Django 4.1.4 on 2023-01-05 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0008_alter_product_crud_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_crud',
            name='Size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
