import json
import os
from django.shortcuts import render
from django.conf import settings
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe_list.html", {"recipes": recipes})

def recipe_detail(request, recipe_id):
    try: 
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        recipe = None
    return render(request, "recipe_details.html", {"recipe": recipe})