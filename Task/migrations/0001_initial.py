# Generated by Django 3.0.3 on 2020-02-22 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Level', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('content', models.CharField(max_length=2048)),
                ('answer', models.CharField(max_length=512)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('level_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Level.Level')),
            ],
        ),
    ]