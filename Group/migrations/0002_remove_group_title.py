# Generated by Django 3.0.3 on 2020-02-22 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='title',
        ),
    ]
