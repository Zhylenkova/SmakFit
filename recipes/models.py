from django.db import models

class Ingredient(models.Model):
   UNIT_CHOICES = [
      ("g", "gram"),
      ("ml", "milliliter"),
      ("pcs", "piece")
   ]

   name = models.CharField(max_length=120, unique=True)
   unit = models.CharField(max_length=8, choices=UNIT_CHOICES, default="g")
   kcal=models.FloatField()
   protein=models.FloatField()
   fat=models.FloatField()
   carbs=models.FloatField()

   def __str__(self):
      return self.name

class Recipe(models.Model):
  name = models.CharField(max_length=160)
  instructions = models.TextField(blank=True)
  kcal = models.FloatField(default=0)
  protein = models.FloatField(default=0)
  fat = models.FloatField(default=0)
  carbs = models.FloatField(default=0)
  tags = models.JSONField(default=list, blank=True)
  time_minutes = models.IntegerField(default=10)
  cost_est = models.FloatField(default=0.0)
  
  def __str__(self):
      return self.name
  

class RecipeIngredient(models.Model):
   recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="items")
   ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
   amount = models.FloatField(help_text="Amount in units")
   portion_base = models.FloatField(default=1.0)