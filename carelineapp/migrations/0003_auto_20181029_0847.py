# Generated by Django 2.0.8 on 2018-10-29 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carelineapp', '0002_topic_topic_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_id',
            field=models.IntegerField(help_text='Topic ID must be unique', unique=True),
        ),
    ]
