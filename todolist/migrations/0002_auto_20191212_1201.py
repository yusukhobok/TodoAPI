# Generated by Django 3.0 on 2019-12-12 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoList',
            new_name='Todo',
        ),
    ]