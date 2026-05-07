from django.contrib import admin
from .models import Dish, Category


@admin.register(Dish)
class CatalogAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass