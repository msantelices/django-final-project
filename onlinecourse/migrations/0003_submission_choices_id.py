# Generated by Django 3.1.3 on 2022-06-05 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20220605_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='choices_id',
            field=models.JSONField(default=list),
        ),
    ]
