# Generated by Django 3.0.8 on 2020-08-02 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200802_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='episode_id',
            field=models.IntegerField(null=True),
        ),
    ]
