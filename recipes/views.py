from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe

@api_view(["GET", "POST"])
def recipe_list(request):
  if request.method == "POST":
    data=request.data
    r = Recipe.objects.create(
      name=data["name"],
      kcal = data.get("kcal", 0),
      protein = data.get("kcal", 0),
      fat = data.get("fat", 0),
      carbs = data.get("carbs", 0),
      tags = data.get("tags", [])
    )
    return Response({"id": r.id}, status=201)
  
  items = list(Recipe.objects.values())
  return Response(items)


