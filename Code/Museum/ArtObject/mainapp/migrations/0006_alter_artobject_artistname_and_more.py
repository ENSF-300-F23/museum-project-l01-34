# Generated by Django 4.2.7 on 2023-11-30 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_artobject_artdesc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artobject',
            name='ArtistName',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='mainapp.artist'),
        ),
        migrations.AlterField(
            model_name='artobject',
            name='ExhibitName',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='mainapp.exhibition'),
        ),
    ]
