# Generated by Django 3.2.6 on 2021-12-07 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_codeit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codeit',
            name='prob',
        ),
    ]
