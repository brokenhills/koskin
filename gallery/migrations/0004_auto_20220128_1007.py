# Generated by Django 3.2.5 on 2022-01-28 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20160818_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='gallery',
            name='img',
            field=models.FileField(upload_to='media/', verbose_name='Фотография'),
        ),
    ]
