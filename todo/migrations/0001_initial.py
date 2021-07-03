# Generated by Django 3.2.4 on 2021-06-27 21:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField(verbose_name=datetime.date)),
                ('work_status', models.CharField(choices=[('todo', 'todo'), ('doing', 'doing'), ('done', 'done')], default='todo', max_length=5)),
            ],
        ),
    ]
