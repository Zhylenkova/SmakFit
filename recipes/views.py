from rest_framework import viewsets
from rest_framework.response import Response
from .models import Recipe, Ingredient
from .serializers import IngredientSerializer, RecipeSerializer

class IngredientViewSet(viewsets.ModelViewSet):
  queryset = Ingredient.objects.all().order_by("name")
  serializer_class=IngredientSerializer

class RecipeViewSet(viewsets.ModelViewSet):
  queryset = Recipe.objects.all().order_by("name")
  serializer_class = RecipeSerializer


