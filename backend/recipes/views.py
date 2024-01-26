from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Recipe, Product, RecipeProduct
from .serializers import RecipeSerializer
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
    product = get_object_or_404(Product, id=product_id)
    recipes_without_product = Recipe.objects.exclude(recipeproduct__product__id=product_id).distinct()

    serializer = RecipeSerializer(recipes_without_product, many=True)

    return render(request, 'show_recipes_without_product.html', {'recipes': serializer.data})

