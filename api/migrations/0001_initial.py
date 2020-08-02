# Generated by Django 3.0.8 on 2020-08-01 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('height', models.IntegerField()),
                ('mass', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('episode_id', models.IntegerField()),
                ('opening_crawl', models.CharField(max_length=1200)),
                ('director', models.CharField(max_length=120)),
                ('producer', models.CharField(max_length=120)),
                ('characters', models.ManyToManyField(to='api.Character')),
            ],
        ),
    ]