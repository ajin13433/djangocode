# Generated by Django 3.2.6 on 2021-12-17 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_alter_solutions_verdict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='code',
            field=models.TextField(blank='true'),
        ),
    ]