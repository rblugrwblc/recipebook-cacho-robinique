from django.urls import path
from . import views

urlpatterns = [
    path("recipes/list/", views.recipe_list, name="recipe_list"),  
    path("recipe/<int:recipe_id>/", views.recipe_detail, name="recipe_detail"),
    path("recipe/add/", views.add_recipe, name="add_recipe"),
    path("recipe/<int:recipe_id>/add_image/", views.add_recipe_image, name="add_recipe_image"),
]