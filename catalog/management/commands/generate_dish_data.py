from random import choice

from django.core.management import BaseCommand
from faker.proxy import Faker
from catalog.models import Dish, Category


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()

        dish_names = [
            "Паста карбонара",
            "Цезарь с курицей",
            "Том-ям",
            "Сырники",
            "Борщ",
            "Пицца Маргарита",
        ]
        categories = list(Category.objects.all())

        for _ in range(40):
            Dish.objects.create(
                category=choice(categories),
                name=choice(dish_names),
                description=fake.text(),
                weight=fake.random_int(),
                price=fake.random_int(200, 6000)
            )

        self.stdout.write(
            self.style.SUCCESS("Создано 40 блюд")
        )