# Generated by Django 4.1.4 on 2023-01-27 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0045_rename_useradmin_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='Name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='UserType',
            field=models.CharField(choices=[('admin', 'Admin'), ('staff', 'Staff')], max_length=50),
        ),
    ]
