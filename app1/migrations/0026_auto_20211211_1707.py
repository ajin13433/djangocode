# Generated by Django 3.2.6 on 2021-12-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_alter_solutions_verdict'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='test',
            name='op',
        ),
        migrations.AddField(
            model_name='test',
            name='index',
            field=models.IntegerField(max_length=50, null='true'),
            preserve_default='true',
        ),
    ]
