from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from django.db.models import Sum, Case, When, IntegerField, F
from django.db import transaction
from .models import Recipe, Product, RecipeProduct


@api_view(['GET'])
def add_product_to_recipe(request, recipe_id, product_id, weight):
    try:
        weight = int(weight)
    except ValueError:
        return Response({'status': 'error', 'message': 'Invalid weight format'}, status=status.HTTP_400_BAD_REQUEST)

    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)

    with transaction.atomic():
        recipe_product, created = RecipeProduct.objects.get_or_create(
            recipe=recipe, product=product, defaults={'weight': weight})

        if not created:
            recipe_product.weight = weight
            recipe_product.save()

    return Response({
            'status': 'success',
            'message': f'Product {product.name} {weight}g added to recipe {recipe.name}'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@transaction.atomic
def cook_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    try:
        with transaction.atomic():
            for product in recipe.products.all():
                product.cooked = F('cooked') + 1
                product.save(update_fields=['cooked'])
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({'status': 'success', 'message': f'Recipe cooked: {recipe.name}'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def show_recipes_without_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    recipes_without_product = (
        Recipe.objects
        .annotate(product_weight=Sum(
            Case(
                When(recipeproduct__product=product, then='recipeproduct__weight'),
                default=0,
                output_field=IntegerField()
            )
        ))
        .exclude(product_weight__gte=10)
        .distinct()
    )

    return render(request, 'show_recipes_without_product.html', {'recipes': recipes_without_product})
