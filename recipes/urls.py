from django.urls import path
from .views import IngredientViewSet, RecipeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"ingredients", IngredientViewSet)
router.register(r"recipes", RecipeViewSet)

urlpatterns = router.urls
