# Generated by Django 4.2.7 on 2023-12-05 11:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('ArtistName', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('DateBorn', models.IntegerField(blank=True, null=True)),
                ('DateDied', models.IntegerField(blank=True, null=True)),
                ('CountryOfOrigin', models.CharField(blank=True, max_length=20)),
                ('MainStyle', models.CharField(blank=True, max_length=20)),
                ('Epoch', models.CharField(blank=True, max_length=20)),
                ('ArtistDesc', models.CharField(blank=True, max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ArtObject',
            fields=[
                ('IdNo', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('Title', models.CharField(default='Unknown', max_length=60)),
                ('YearMade', models.IntegerField(blank=True, null=True)),
                ('Origin', models.CharField(blank=True, max_length=20)),
                ('Style', models.CharField(blank=True, max_length=20)),
                ('Epoch', models.CharField(blank=True, max_length=20)),
                ('ArtDesc', models.CharField(blank=True, max_length=60)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg']), mainapp.models.ValidateImageFile])),
                ('ArtistName', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('CollName', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('CollType', models.CharField(max_length=15)),
                ('Phone', models.CharField(max_length=15)),
                ('ContactPerson', models.CharField(blank=True, max_length=20)),
                ('Epoch', models.CharField(blank=True, max_length=20)),
                ('CollDesc', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('ExhibitName', models.SlugField(max_length=80, primary_key=True, serialize=False)),
                ('StartDate', models.DateField(blank=True, null=True)),
                ('EndDate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('IdNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mainapp.artobject')),
                ('ArtType', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('IdNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mainapp.artobject')),
                ('PaintType', models.CharField(blank=True, max_length=15)),
                ('DrawnOn', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PermanentCollection',
            fields=[
                ('IdNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mainapp.artobject')),
                ('DateAquired', models.DateField(blank=True, null=True)),
                ('PcollStatus', models.CharField(max_length=10)),
                ('Cost', models.DecimalField(decimal_places=4, max_digits=19, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SculptureOrStatue',
            fields=[
                ('IdNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mainapp.artobject')),
                ('Material', models.CharField(blank=True, max_length=50, null=True)),
                ('Height', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('Weight', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DisplayedIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExhibitName', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.exhibition')),
                ('IdNo', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.artobject')),
            ],
        ),
        migrations.CreateModel(
            name='Borrowed',
            fields=[
                ('IdNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mainapp.artobject')),
                ('DateBorrowed', models.DateField(blank=True, null=True)),
                ('DateReturned', models.DateField(blank=True, null=True)),
                ('CollName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.collection')),
            ],
        ),
    ]