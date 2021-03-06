# Generated by Django 3.0.7 on 2020-06-25 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0003_auto_20200624_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='additional_info',
            field=models.TextField(default=None, max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='dietary_requirements',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='favourite_drink',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='favourite_song',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='not_attending',
            field=models.CharField(max_length=100),
        ),
    ]
