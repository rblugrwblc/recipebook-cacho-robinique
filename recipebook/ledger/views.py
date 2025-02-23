import json
import os
from django.shortcuts import render
from django.conf import settings

def load_recipes():
    file_path = os.path.join(settings.BASE_DIR, "ledger", "static", "Recipe List Context.txt")

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)["recipes"] 

def recipe_list(request):
    recipes = load_recipes()

    return render(request, "recipe_list.html", {"recipes": recipes})

def recipe_detail(request, recipe_id):
    recipes = load_recipes()
    recipe = next((r for r in recipes if f"/recipe/{recipe_id}" == r["link"]), None)

    return render(request, "recipe_details.html", {"recipe": recipe})