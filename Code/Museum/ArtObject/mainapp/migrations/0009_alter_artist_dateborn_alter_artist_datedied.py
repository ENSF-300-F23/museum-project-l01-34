# Generated by Django 4.2.7 on 2023-12-03 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_other'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='DateBorn',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='DateDied',
            field=models.IntegerField(null=True),
        ),
    ]
