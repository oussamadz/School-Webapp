# Generated by Django 3.1 on 2020-12-17 23:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cours_start',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]