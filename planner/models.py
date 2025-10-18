from django.db import models

class MealPlan(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  days = models.IntegerField(default=7)
  meals_per_day = models.IntegerField(default=4)
  target_kcal = models.IntegerField(default = 2000)
