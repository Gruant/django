# Generated by Django 2.2.8 on 2020-02-09 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site_app', '0006_auto_20200209_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.PositiveIntegerField(default=0, verbose_name='Сумма'),
        ),
    ]
