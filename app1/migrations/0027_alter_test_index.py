# Generated by Django 3.2.6 on 2021-12-11 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_auto_20211211_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='index',
            field=models.IntegerField(null='true'),
        ),
    ]