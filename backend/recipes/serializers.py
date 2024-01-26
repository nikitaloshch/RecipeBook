from rest_framework import serializers
from .models import Recipe, Product, RecipeProduct


class RecipeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeProduct
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {'id': representation['id'], 'name': representation['name']}
