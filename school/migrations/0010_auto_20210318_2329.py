# Generated by Django 3.1 on 2021-03-18 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='photo',
            field=models.ImageField(default='default-events.jpg', upload_to='events_pics'),
        ),
    ]
