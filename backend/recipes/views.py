from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Recipe, Product, RecipeProduct
from django.shortcuts import render


@api_view(['GET'])
def add_product_to_recipe(request, recipe_id, product_id, weight):
    try:
        weight = int(weight)
    except ValueError:
        return Response({'status': 'error', 'message': 'Invalid weight format'}, status=status.HTTP_400_BAD_REQUEST)

    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)

    recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product, defaults={'weight': weight})

    if not created:
        recipe_product.weight = weight
        recipe_product.save()

    return Response({'status': 'success', 'message': 'Product added to recipe'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def cook_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    products = recipe.products.all()

    for product in products:
        product.cooked += 1
        product.save()

    return Response({'status': 'success', 'message': f'Recipe cooked: {recipe.name}'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def show_recipes_without_product(request, product_id):
    try:
        product_id = int(product_id)
    except ValueError:
        return Response({'status': 'error', 'message': 'Invalid product ID'}, status=status.HTTP_400_BAD_REQUEST)

    # Получим рецепты, которые не связаны с указанным продуктом
    recipes_without_product = Recipe.objects.exclude(recipeproduct__product__id=product_id)

    # Добавим условие для отсеивания рецептов, где вес продукта больше или равен 10 граммам
    recipes_without_product = [recipe for recipe in recipes_without_product if all(rp.weight < 10 for rp in recipe.recipeproduct_set.filter(product__id=product_id))]

    # Возвращаем HTML-страницу с использованием шаблона
    return render(request, 'show_recipes_without_product.html', {'recipes': recipes_without_product})

