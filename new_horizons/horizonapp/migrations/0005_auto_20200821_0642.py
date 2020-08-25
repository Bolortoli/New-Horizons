# Generated by Django 3.0.7 on 2020-08-21 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('horizonapp', '0004_auto_20200821_0632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='or_detail',
        ),
        migrations.AddField(
            model_name='organizationdetail',
            name='organization',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='horizonapp.Organization', verbose_name='Байгуулага'),
        ),
    ]