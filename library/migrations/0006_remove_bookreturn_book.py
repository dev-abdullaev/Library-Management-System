# Generated by Django 3.2.6 on 2021-08-24 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("library", "0005_auto_20210823_1727")]

    operations = [migrations.RemoveField(model_name="bookreturn", name="book")]
