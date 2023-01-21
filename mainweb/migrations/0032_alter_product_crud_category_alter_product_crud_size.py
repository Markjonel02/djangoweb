# Generated by Django 4.1.4 on 2023-01-20 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0031_alter_photoup_category_alter_photoup_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_crud',
            name='Category',
            field=models.CharField(choices=[('adhesive', 'Adhesive'), ('porcelain', 'Porcelain'), ('ceramic', 'Ceramic'), ('skimcoat', 'Skimcoat'), ('sanitaryware ', 'Sanitary ware')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product_crud',
            name='Size',
            field=models.CharField(blank=True, choices=[('12 x 30', '12 x 30'), ('247 x 97', '247 x 97'), ('20 x 30', '20 x 30')], max_length=50, null=True),
        ),
    ]
