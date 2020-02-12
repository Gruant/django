from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.template.defaultfilters import slugify


class Product(models.Model):
    title = models.CharField(max_length=128, verbose_name='Наименование')
    description = models.TextField(max_length=500, verbose_name='Описание')
    image = models.ImageField(upload_to='media',
                              verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория', null=True, blank=True)
    price = models.FloatField(default=0, verbose_name='Цена')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(MPTTModel):
    name = models.CharField(max_length=64, unique=True, verbose_name='Категория')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE,
                            db_index=True, verbose_name='Родительская категория')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Collection(models.Model):
    title = models.CharField(max_length=128, verbose_name='Коллекция')
    description = models.TextField(max_length=450, verbose_name='Описание')
    products = models.ManyToManyField(Product, related_name='collections')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    ordering = ['created']

    def __str__(self):
        return str(self.title) + ' ' + str(self.created)


class Basket(models.Model):
    uid = models.CharField(max_length=150, blank=True, null=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    items = models.ManyToManyField(Product, through='ProductInBasket', related_name='basket')


class ProductInBasket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    count = models.IntegerField()


class Order(models.Model):
    product = models.ManyToManyField('Product', related_name='order', verbose_name='Товары',
                                     through='ProductOrder')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Покупатель', default='')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    total = models.PositiveIntegerField(verbose_name='Сумма', default=0)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.buyer) + ' ' + str(self.created)


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(verbose_name='Кол-во', default=1)
    total = models.PositiveIntegerField(verbose_name='Сумма', default=0)

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товар в заказах'

    def __str__(self):
        return str(self.order) + ' ' + str(self.product)


class Review(models.Model):
    text = models.CharField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    rating = models.PositiveIntegerField(verbose_name='Оценка')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Автор')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return str(self.product) + ' ' + str(self.text)



