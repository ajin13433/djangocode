# Generated by Django 3.2.6 on 2021-12-07 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20211207_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solutions',
            name='code',
            field=models.TextField(),
        ),
    ]
