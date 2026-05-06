from django.contrib import admin
from .models import Dish

@admin.register(Dish)
class CatalogAdmin(admin.ModelAdmin):
    pass