# Generated by Django 3.2.6 on 2021-12-07 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_remove_codeit_prob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeit',
            name='code',
            field=models.TextField(blank='true'),
        ),
    ]
