# Generated by Django 3.0 on 2020-08-03 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0008_auto_20200803_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='lastChangeDateTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
