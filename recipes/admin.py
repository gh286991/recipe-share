from django.contrib import admin
from recipes.models import Recipe
# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Recipe, RecipeAdmin)
