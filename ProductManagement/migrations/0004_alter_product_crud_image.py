# Generated by Django 4.1.3 on 2023-06-03 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManagement', '0003_alter_product_crud_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_crud',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='product/'),
        ),
    ]
