from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeIngredient

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe_list.html", {
        "recipes": recipes,
        "page_title": "Recipe List"  
    })

@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = recipe.recipe_ingredients.all()  
    return render(request, "recipe_detail.html", {
        "recipe": recipe,
        "ingredients": ingredients
    })