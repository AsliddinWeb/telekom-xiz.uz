# Generated by Django 5.0 on 2023-12-08 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twoheaderservices',
            name='service_category',
        ),
        migrations.DeleteModel(
            name='TwoHeaderServiceCategory',
        ),
        migrations.DeleteModel(
            name='TwoHeaderServices',
        ),
    ]
