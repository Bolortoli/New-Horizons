# Generated by Django 3.0.7 on 2020-08-20 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horizonapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='pic',
        ),
    ]