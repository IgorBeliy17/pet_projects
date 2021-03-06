# Generated by Django 3.2.7 on 2021-11-13 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=40, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Топпинг',
                'verbose_name_plural': 'Топпинги',
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Фото')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='ЧПУ')),
                ('created_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
                ('toppings', models.ManyToManyField(to='pizza.Topping', verbose_name='Топпинги')),
            ],
            options={
                'verbose_name': 'Пицца',
                'verbose_name_plural': 'Пиццы',
            },
        ),
    ]
