# Generated by Django 4.0.1 on 2022-01-24 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
