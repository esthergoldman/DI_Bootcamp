# Generated by Django 3.1.7 on 2021-03-04 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='gifs',
            field=models.ManyToManyField(to='info.Gif'),
        ),
    ]
