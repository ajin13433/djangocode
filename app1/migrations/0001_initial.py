# Generated by Django 3.2.6 on 2021-12-05 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='porblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('name', models.CharField(max_length=1000)),
                ('statement', models.TextField()),
            ],
        ),
    ]
