# Generated by Django 3.0.7 on 2020-07-04 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0004_auto_20200625_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecarousel',
            name='image',
            field=models.ImageField(upload_to='carousel/home/'),
        ),
        migrations.AlterField(
            model_name='villacarousel',
            name='image',
            field=models.ImageField(upload_to='carousel/villa/'),
        ),
    ]