from django.db import models

class Recipe(models.Model):
  name = models.CharField(max_length=160)
  kcal = models.FloatField(default=0)
  protein = models.FloatField(default=0)
  fat = models.FloatField(default=0)
  carbs = models.FloatField(default=0)
  tags = models.JSONField(default=list, blank=True)
  
  def __str__(self):
      return self.name