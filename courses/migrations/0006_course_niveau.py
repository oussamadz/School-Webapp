# Generated by Django 3.1 on 2020-12-28 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20201221_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='niveau',
            field=models.CharField(choices=[('1-primaire', '1_pri'), ('2-primaire', '2_pri'), ('3-primaire', '3_pri'), ('4-primaire', '4_pri'), ('5-primaire', '5_pri'), ('1-moyenne', '1_moy'), ('2-moyenne', '2_moy'), ('3-moyenne', '3_moy'), ('4-moyenne', '4_moy'), ('1-secondaire', '1_sec'), ('2-secondaire', '21_sec'), ('3-secondaire', '31_sec')], default='1_pri', max_length=100),
        ),
    ]