# Generated by Django 2.2.6 on 2021-06-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queues', '0005_auto_20210616_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='lati',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
        migrations.AlterField(
            model_name='queue',
            name='longi',
            field=models.DecimalField(decimal_places=20, max_digits=25),
        ),
    ]
