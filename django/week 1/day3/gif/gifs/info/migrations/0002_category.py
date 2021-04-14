# Generated by Django 3.1.7 on 2021-03-03 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('field_name', models.URLField()),
                ('uploader_name', models.CharField(max_length=30)),
                ('created_at', models.DateField()),
            ],
        ),
    ]
