# Generated by Django 5.1.4 on 2024-12-16 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0004_authordetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authordetails',
            name='id',
        ),
        migrations.AlterField(
            model_name='authordetails',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='details', serialize=False, to='my_first_app.author'),
        ),
    ]
