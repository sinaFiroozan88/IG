from django.contrib import admin
from .models import Food, Ingredient, DailyMeal

admin.site.register(Food)
admin.site.register(Ingredient)
admin.site.register(DailyMeal)

