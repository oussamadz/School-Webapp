# Generated by Django 3.1 on 2021-02-05 17:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='cours_start',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]