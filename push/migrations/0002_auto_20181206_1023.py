# Generated by Django 2.0.8 on 2018-12-06 10:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('push', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pushnotify',
            name='device',
        ),
        migrations.AddField(
            model_name='pushnotify',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
