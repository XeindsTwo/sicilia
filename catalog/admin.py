from django.contrib import admin
from django.db import models
from image_uploader_widget.widgets import ImageUploaderWidget
from .models import Dish, Category


@admin.register(Dish)
class CatalogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ImageField: {'widget': ImageUploaderWidget}
    }

    list_display = ["name", "category", "description", "price", "weight"]

    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "is_available",
                    "category",
                    "name",
                    "description",
                    "price",
                    "weight",
                    "image",
                ),
            },
        ),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "order")
    ordering = ("-order",)
