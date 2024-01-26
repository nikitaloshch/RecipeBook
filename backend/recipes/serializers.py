from rest_framework import serializers
from .models import Recipe, Product, RecipeProduct


class RecipeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeProduct
        fields = ['recipe', 'product', 'weight']


class RecipeSerializer(serializers.ModelSerializer):
    products = RecipeProductSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'products']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']