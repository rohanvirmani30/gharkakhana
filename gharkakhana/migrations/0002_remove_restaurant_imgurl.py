# Generated by Django 3.0.5 on 2020-04-20 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gharkakhana', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='imgurl',
        ),
    ]
