from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import ImageField, ForeignKey
from django.db.models.fields import CharField, IntegerField


class Category(models.Model):
    name = CharField(
        max_length=255,
        verbose_name="Название категории"
    )
    description = CharField(
        max_length=255,
        verbose_name="Описание категории"
    )
    order = IntegerField(unique=True, editable=False)

    class Meta:
        ordering = ['order']

class Dish(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название блюда"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Название блюда"
    )
    weight = models.IntegerField(
        verbose_name="Вес блюда",
        validators=[
            MinValueValidator(1),
            MaxValueValidator(20000)
        ]
    )
    price = models.IntegerField(verbose_name="Цена блюда")
    image = ImageField(verbose_name="Изображение блюда")
    category = ForeignKey(Category, related_name="categories", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "блюдо"
        verbose_name_plural = "Блюда"