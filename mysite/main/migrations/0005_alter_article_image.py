# Generated by Django 4.0.1 on 2022-01-18 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]