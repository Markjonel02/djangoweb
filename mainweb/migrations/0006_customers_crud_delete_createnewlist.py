# Generated by Django 4.1.4 on 2022-12-28 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0005_alter_createnewlist_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers_crud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomersName', models.CharField(max_length=20)),
                ('ContactNumber', models.IntegerField()),
                ('CustomersEmail', models.EmailField(max_length=254)),
                ('CustomersAdd', models.TextField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='CreateNewList',
        ),
    ]
