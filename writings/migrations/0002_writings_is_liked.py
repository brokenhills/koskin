# Generated by Django 3.2.5 on 2022-01-28 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='writings',
            name='is_liked',
            field=models.BooleanField(default=0, verbose_name='Избранное'),
        ),
    ]
