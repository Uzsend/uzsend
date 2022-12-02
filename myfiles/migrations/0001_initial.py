# Generated by Django 4.1.2 on 2022-12-02 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasim', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=40)),
                ('rasim', models.ImageField(upload_to='media')),
                ('nomi', models.CharField(max_length=20)),
                ('tafsiya', models.CharField(max_length=200)),
            ],
        ),
    ]
