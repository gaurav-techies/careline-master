# Generated by Django 2.0.8 on 2018-11-19 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carelineapp', '0006_auto_20181108_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='counselling_topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
    ]
