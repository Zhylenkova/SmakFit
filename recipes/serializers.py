from rest_framework import serializers
from .models import Ingredient, Recipe, RecipeIngredient

class IngredientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ingredient
    fields = "__all__"

class RecipeIngredientInlineSerializer(serializers.ModelSerializer):
  ingredient = IngredientSerializer(read_only=True)
  ingredient_id = serializers.PrimaryKeyRelatedField(
    queryset=Ingredient.objects.all(), source="ingredient", write_only=True
  )
  class Meta:
    model=RecipeIngredient
    fields=("id","ingredient","ingredient_id","amount","portion_base")

class RecipeSerializer(serializers.ModelSerializer):
  items = RecipeIngredientInlineSerializer(many=True, required=False)

  class Meta:
    model = Recipe
    fields = (
      "id","name","instructions","tags","time_minutes","cost_est",
      "kcal","protein","fat","carbs","items"
    )    
    def create(self, validated_data):
      items = validated_data.pop("items", [])
      recipe = Recipe.objects.create(**validated_data)
      for item in items:
        RecipeIngredient.objects.create(recipe=recipe, **item)
      return recipe
    
    def update(self, instance, validated_data):
      items=validated_data.pop("items", None)
      for k,v in validated_data.items():
        setattr(instance, k, v)
      instance.save()
      if items is not None:
        instance.items.all().delete()
        for item in items:
          RecipeIngredient.object.create(recipe=instance, **item)
        return instance 