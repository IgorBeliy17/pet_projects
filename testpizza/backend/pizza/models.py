from django.db import models
from django.utils.timezone import now
from django.conf import settings
# from django.contrib.auth.models import User


class Topping(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название', )
    description = models.CharField(max_length=40, verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'


class Pizza(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    toppings = models.ManyToManyField(Topping, verbose_name='Топпинги')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото', blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', default=now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Кем создано')
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(verbose_name='ЧПУ', blank=True, unique=True, null=True)

    def __str__(self):
        return self.name

    def is_valid_pizza(self):
        return self.name != 0 and self.toppings != 0 and self.description != 0

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'






