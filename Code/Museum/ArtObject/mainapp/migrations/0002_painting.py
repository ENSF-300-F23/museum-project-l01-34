# Generated by Django 4.2.7 on 2023-11-30 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('IdNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mainapp.artobject')),
                ('PaintType', models.CharField(blank=True, max_length=15)),
                ('DrawnOn', models.CharField(blank=True, max_length=15)),
            ],
        ),
    ]