# Generated by Django 3.0.8 on 2020-08-02 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_planet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planet',
            name='film',
        ),
        migrations.AddField(
            model_name='planet',
            name='films',
            field=models.ManyToManyField(to='api.Film'),
        ),
    ]
