# Generated by Django 3.2.6 on 2021-08-19 20:16

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20210819_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='issue_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='return_date',
            field=models.DateField(default=library.models.get_expiry_date, null=True),
        ),
    ]