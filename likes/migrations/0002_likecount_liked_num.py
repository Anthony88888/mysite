# Generated by Django 2.0.13 on 2020-10-13 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='likecount',
            name='liked_num',
            field=models.IntegerField(default=0),
        ),
    ]
