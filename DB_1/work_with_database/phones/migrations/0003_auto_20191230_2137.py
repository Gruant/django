# Generated by Django 2.1.1 on 2019-12-30 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_auto_20191230_2128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='lte_exist',
            new_name='lte_exists',
        ),
    ]
