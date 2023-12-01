# Generated by Django 4.2.7 on 2023-11-30 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_artobject_artistname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artobject',
            name='ArtistName',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.artist'),
        ),
        migrations.AlterField(
            model_name='artobject',
            name='ExhibitName',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.exhibition'),
        ),
    ]