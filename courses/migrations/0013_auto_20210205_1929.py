# Generated by Django 3.1 on 2021-02-05 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20210205_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='wday1',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Dimanche', 'Dim'), ('Lundi', 'Lun'), ('Mardi', 'Mar'), ('Mercredi', 'Mer'), ('Jeudi', 'Jeu'), ('Vendredi', 'Ven'), ('Samedi', 'Sam')], default='N/A', max_length=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='wday2',
            field=models.CharField(choices=[('N/A', 'N/A'), ('Dimanche', 'Dim'), ('Lundi', 'Lun'), ('Mardi', 'Mar'), ('Mercredi', 'Mer'), ('Jeudi', 'Jeu'), ('Vendredi', 'Ven'), ('Samedi', 'Sam')], default='N/A', max_length=10),
        ),
    ]
