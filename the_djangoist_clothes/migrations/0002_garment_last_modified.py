# Generated by Django 2.1.2 on 2018-10-23 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_djangoist_clothes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='garment',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
