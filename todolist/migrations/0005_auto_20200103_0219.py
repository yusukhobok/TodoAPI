# Generated by Django 3.0 on 2020-01-02 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_remove_todo_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catTitle', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todolist.Category'),
            preserve_default=False,
        ),
    ]
