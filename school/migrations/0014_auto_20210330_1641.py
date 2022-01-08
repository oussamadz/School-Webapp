# Generated by Django 3.1 on 2021-03-30 14:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_galleryimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='admission',
            name='sub_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='student',
            name='cours_start',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Expiration Date'),
        ),
    ]