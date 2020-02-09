# Generated by Django 2.2.8 on 2020-02-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site_app', '0005_auto_20200209_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='anonymous_user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.AlterField(
            model_name='order',
            name='buyer',
            field=models.CharField(default='', max_length=150, verbose_name='Покупатель'),
        ),
    ]
