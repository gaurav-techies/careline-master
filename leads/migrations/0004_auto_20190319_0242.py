# Generated by Django 2.0.8 on 2019-03-19 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_auto_20190319_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaddb',
            name='bitly_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
