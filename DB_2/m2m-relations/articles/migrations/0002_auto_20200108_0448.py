# Generated by Django 2.2.8 on 2020-01-08 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintopic',
            name='is_main',
            field=models.BooleanField(verbose_name='ОСНОВНАЯ'),
        ),
    ]
