# Generated by Django 3.1 on 2021-01-26 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20210116_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='presence',
            field=models.TextField(default='--'),
        ),
    ]
