# Generated by Django 3.1.4 on 2021-01-16 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_time2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='niveau',
            field=models.CharField(choices=[('N/A', 'N/A'), ('1-primaire', '1_pri'), ('2-primaire', '2_pri'), ('3-primaire', '3_pri'), ('4-primaire', '4_pri'), ('5-primaire', '5_pri'), ('1-moyenne', '1_moy'), ('2-moyenne', '2_moy'), ('3-moyenne', '3_moy'), ('4-moyenne', '4_moy'), ('1-secondaire', '1_sec'), ('2-secondaire', '21_sec'), ('3-secondaire', '31_sec')], default='1_pri', max_length=100),
        ),
    ]
