# Generated by Django 3.1 on 2021-03-26 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_auto_20210128_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='professionalExperience',
            field=models.TextField(default='N/A'),
        ),
    ]
