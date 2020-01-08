from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Topic(models.Model):

    name = models.CharField(max_length=64, verbose_name='Тематика')
    articles = models.ManyToManyField(Article, related_name='topics', through='MainTopic')

    class Meta:
        verbose_name = 'Темы'

    def __str__(self):
        return self.name


class MainTopic(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='ОСНОВНАЯ')

    class Meta:
        ordering = ['-is_main', '-topic']




