# Generated by Django 3.2.7 on 2021-11-17 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizza', '0002_alter_pizza_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кем создано'),
        ),
    ]
