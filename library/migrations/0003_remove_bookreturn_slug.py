# Generated by Django 3.2.6 on 2021-08-22 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookreturn',
            name='slug',
        ),
    ]