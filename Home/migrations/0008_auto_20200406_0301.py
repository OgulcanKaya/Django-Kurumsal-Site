# Generated by Django 3.0.4 on 2020-04-06 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_auto_20200406_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='map',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
