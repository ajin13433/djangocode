# Generated by Django 3.2.6 on 2021-12-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_auto_20211208_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solutions',
            name='code',
        ),
        migrations.AddField(
            model_name='problem',
            name='code',
            field=models.TextField(blank='true'),
        ),
    ]