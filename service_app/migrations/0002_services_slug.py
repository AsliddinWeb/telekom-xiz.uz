# Generated by Django 5.0 on 2023-12-08 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='slug',
            field=models.SlugField(blank=True, max_length=455, null=True),
        ),
    ]
