# Generated by Django 2.2.8 on 2020-01-08 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст')),
                ('published_at', models.DateTimeField(verbose_name='Дата публикации')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='MainTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False, verbose_name='ОСНОВНАЯ')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
            options={
                'ordering': ['-is_main', '-topic'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Тематика')),
                ('articles', models.ManyToManyField(related_name='topics', through='articles.MainTopic', to='articles.Article')),
            ],
            options={
                'verbose_name': 'Темы',
            },
        ),
        migrations.AddField(
            model_name='maintopic',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Topic'),
        ),
    ]
