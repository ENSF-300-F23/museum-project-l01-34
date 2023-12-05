# Generated by Django 4.2.7 on 2023-12-05 11:19

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_artobject_image'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='artobject',
            constraint=models.CheckConstraint(check=models.Q(('Image', django.db.models.expressions.CombinedExpression(models.F('IdNo'), '+', models.Value('.jpg')))), name='ImageNameConstraint'),
        ),
    ]