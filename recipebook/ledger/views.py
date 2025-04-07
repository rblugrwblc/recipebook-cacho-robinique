from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import RecipeForm, RecipeImageForm
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage

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
    images = recipe.images.all()
    return render(request, "recipe_detail.html", {
        "recipe": recipe,
        "ingredients": ingredients,
        "images": images
    })

@login_required
def add_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            # Handle ingredients
            ingredient_ids = request.POST.getlist('ingredient')
            quantities = request.POST.getlist('quantity')
            
            for ingredient_id, quantity in zip(ingredient_ids, quantities):
                if ingredient_id and quantity:
                    ingredient = Ingredient.objects.get(id=ingredient_id)
                    RecipeIngredient.objects.create(
                        recipe=recipe, 
                        ingredient=ingredient, 
                        quantity=quantity
                    )

            return redirect('recipe_list')
    else:
        recipe_form = RecipeForm()
    
    ingredients = Ingredient.objects.all()
    return render(request, 'add_recipe.html', {
        'form': recipe_form,
        'ingredients': ingredients,
    })


@login_required
def add_recipe_image(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeImageForm()
    return render(request, 'add_recipe_image.html', {'form': form, 'recipe': recipe})