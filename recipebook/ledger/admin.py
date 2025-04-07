from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, RecipeImageInline]

admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeImage)