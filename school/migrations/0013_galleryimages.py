# Generated by Django 3.1 on 2021-03-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_auto_20210324_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='galleryImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='gallery_pics')),
            ],
        ),
    ]