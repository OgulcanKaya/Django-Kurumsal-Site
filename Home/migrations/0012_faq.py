# Generated by Django 3.0.4 on 2020-05-21 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0011_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsnumber', models.IntegerField()),
                ('question', models.CharField(max_length=150)),
                ('answer', models.TextField()),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
