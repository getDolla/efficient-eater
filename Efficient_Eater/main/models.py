from django.db import models
from decimal import *

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=80)
    logo = models.ImageField(upload_to='media/logos')
    description = models.TextField()

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=150)
    restaurant = models.CharField(max_length=80)
    type_of_item = models.CharField(max_length=10)
    calories = models.IntegerField() #kcal
    total_fat = models.DecimalField(max_digits=5, decimal_places=1) #grams (g)
    sat_fat = models.DecimalField(max_digits=5, decimal_places=1) #grams (g)
    trans_fat = models.DecimalField(max_digits=5, decimal_places=1) #grams (g)
    cholesterol = models.DecimalField(max_digits=5, decimal_places=1) #milligrams (mg)
    sodium = models.DecimalField(max_digits=6, decimal_places=1) #milligrams (mg)
    carbs = models.DecimalField(max_digits=5, decimal_places=1)#grams (g)
    fiber = models.DecimalField(max_digits=5, decimal_places=1) #grams (g)
    sugar = models.DecimalField(max_digits=5, decimal_places=1) #grams (g)
    protein = models.DecimalField(max_digits=5, decimal_places=1) #grams (g)
    floz = models.DecimalField(max_digits=5, decimal_places=1) #fluid ounces (fl oz)

    #calculated properties
    @property
    def calories_from_fat(self):
        return int(self.total_fat * 9)
    @property
    def calories_from_protein(self):
        return int(self.protein * 4)
    @property
    def calories_from_carbs(self):
        return int(self.carbs * 4)
    @property
    def calories_from_saturated_fat(self):
        return int(self.sat_fat * 9)
    @property
    def protein_efficiency(self):
        return round((self.calories_from_protein / self.calories), 3) if self.calories != 0 else 0  # Calories from protein over total calories
    @property
    def fat_efficiency(self):
        return round((self.calories_from_fat / self.calories), 3) if self.calories != 0 else 0  # Calories from fat over total calories
    @property
    def carbs_efficiency(self):
        return round((self.calories_from_carbs / self.calories), 3) if self.calories != 0 else 0  # Calories from carbs over total calories
    @property
    def cholesterol_per_calorie(self):
        return self.cholesterol / self.calories if self.calories != 0 else 0  # Cholesterol per calorie (mg / kcal)
    @property
    def sugar_per_calorie(self):
        return self.sugar / self.calories if self.calories != 0 else 0  # Sugar per calorie (g / kcal)
    @property
    def fiber_per_calorie(self):
        return self.fiber / self.calories if self.calories != 0 else 0  # Fiber per calorie (g / kcal)
    @property
    def sodium_per_calorie(self):
        return self.sodium / self.calories if self.calories != 0 else 0  # Sodium per calorie (mg /kcal)
    @property
    def sugar_per_floz(self):
        return self.sugar / self.floz if self.type_of_item == 'drink' else 0  # Sugar per fluid ounce (g / fl oz) if item is a drink

    def __str__(self):
        return self.name