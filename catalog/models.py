from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import ImageField, ForeignKey
from django.db.models.fields import CharField, IntegerField, BooleanField


class Category(models.Model):
    name = CharField(
        max_length=255,
        verbose_name="Название категории"
    )
    description = CharField(
        max_length=255,
        verbose_name="Описание категории"
    )
    order = IntegerField(
        default=0,
        verbose_name="Порядок категории"
    )

    class Meta:
        ordering = ['order']
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название блюда"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Описание блюда"
    )
    weight = models.IntegerField(
        verbose_name="Вес блюда",
        validators=[
            MinValueValidator(1),
            MaxValueValidator(20000)
        ]
    )
    is_available = BooleanField(default=True, verbose_name="Активно блюдо")
    price = models.IntegerField(verbose_name="Цена блюда")
    image = ImageField(verbose_name="Изображение блюда")
    category = ForeignKey(
        Category,
        related_name="categories",
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "блюдо"
        verbose_name_plural = "Блюда"
