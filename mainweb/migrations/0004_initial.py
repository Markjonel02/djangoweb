# Generated by Django 4.1.4 on 2022-12-22 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainweb', '0003_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateNewList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=50)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]