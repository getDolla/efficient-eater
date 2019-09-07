class Menu_Item_Extended():
    def __init__(self, name, restaurant, type_of_item, calories, protein, carbs, total_fat, saturated_fat, trans_fat, cholesterol, sodium, sugar, fiber, oz, price):
        self.name = name
        self.restaurant = restaurant
        self.type_of_item = type_of_item #meal or drink
        self.calories = calories
        self.protein = protein #In grams
        self.carbs = carbs #In grams
        self.total_fat = total_fat #In grams
        self.saturated_fat = saturated_fat #In grams
        self.trans_fat = trans_fat #In grams
        self.cholesterol = cholesterol #In milligrams
        self.sodium = sodium #In milligrams
        self.sugar = sugar #In grams
        self.fiber = fiber #In grams
        self.oz = oz
        self.price = price

        #fields from calculations
        self.calories_from_fat = self.total_fat * 9
        self.calories_from_protein = self.protein * 4
        self.calories_from_carbs = self.carbs * 4
        self.protein_efficiency = self.calories_from_protein/self.calories #Calories from protein over total calories
        self.fat_efficiency = self.calories_from_fat/self.calories #Calories from fat over total calories
        self.carbs_efficiency = self.calories_from_carbs/self.calories #Calories from carbs over total calories
        self.price_efficiency = self.calories/self.price #Calories per dollar
        self.sodium_ratio = self.sodium/self.calories #Sodium over total calories
        self.cholesterol_ratio = self.cholesterol/self.calories #Cholesterol over total calories
        self.sugar_ratio = self.sugar/self.calories #Sugar over total calories
        self.fiber_ratio = self.fiber/self.calories #Fiber over total calories
        self.protein_per_dollar = self.protein/self.price
        self.fat_per_dollar = self.total_fat/self.price
        self.carbs_per_dollar = self.carbs/self.price
        self.sugar_per_oz = self.sugar/self.oz if self.type_of_item == 'drink' else None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Menu_Item_With_Price():
    def __init__(self, name, restaurant, type_of_item, calories, protein, carbs, fat, price):
        self.name = name
        self.restaurant = restaurant
        self.type_of_item = type_of_item #meal or drink
        self.calories = calories
        self.protein = protein #In grams
        self.carbs = carbs #In grams
        self.fat = fat #In grams
        self.price = price #In dollars

        #fields from calculations
        self.calories_from_fat = self.fat * 9
        self.calories_from_protein = self.protein * 4
        self.calories_from_carbs = self.carbs * 4
        self.protein_efficiency = self.calories_from_protein/self.calories #Calories from protein over total calories
        self.fat_efficiency = self.calories_from_fat/self.calories #Calories from fat over total calories
        self.carbs_efficiency = self.calories_from_carbs/self.calories #Calories from carbs over total calories
        self.price_efficiency = self.calories/self.price #Calories per dollar
        self.protein_per_dollar = self.protein/self.price
        self.fat_per_dollar = self.fat/self.price
        self.carbs_per_dollar = self.carbs/self.price

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Menu_Item_Simple_Without_Price():
    def __init__(self, name, restaurant, type_of_item, calories, protein, carbs, fat):
        self.name = name
        self.restaurant = restaurant
        self.type_of_item = type_of_item #meal or drink
        self.calories = calories
        self.protein = protein #In grams
        self.carbs = carbs #In grams
        self.fat = fat #In grams

        #fields from calculations
        self.calories_from_fat = self.fat * 9
        self.calories_from_protein = self.protein * 4
        self.calories_from_carbs = self.carbs * 4
        self.protein_efficiency = self.calories_from_protein/self.calories if self.calories != 0 else 0 #Calories from protein over total calories
        self.fat_efficiency = self.calories_from_fat/self.calories if self.calories != 0 else 0 #Calories from fat over total calories
        self.carbs_efficiency = self.calories_from_carbs/self.calories if self.calories != 0 else 0 #Calories from carbs over total calories

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Menu_Item_Extended_Without_Price():
    def __init__(self, name, restaurant, type_of_item, calories, protein, carbs, total_fat, sat_fat, trans_fat, cholesterol, sodium, sugar, fiber, floz):
        self.name = name
        self.restaurant = restaurant
        self.type_of_item = type_of_item #meal or drink
        self.calories = calories
        self.protein = protein #In grams
        self.carbs = carbs #In grams
        self.total_fat = total_fat #In grams
        self.sat_fat = sat_fat #In grams
        self.trans_fat = trans_fat #In grams
        self.cholesterol = cholesterol #In milligrams
        self.sodium = sodium #In milligrams
        self.sugar = sugar #In grams
        self.fiber = fiber #In grams
        self.floz = floz #Fluid Ounces in beverage

        #fields from calculations
        self.calories_from_fat = self.total_fat * 9
        self.calories_from_protein = self.protein * 4
        self.calories_from_carbs = self.carbs * 4
        self.protein_efficiency = self.calories_from_protein/self.calories if self.calories != 0 else 0 #Calories from protein over total calories
        self.fat_efficiency = self.calories_from_fat/self.calories if self.calories != 0 else 0 #Calories from fat over total calories
        self.carbs_efficiency = self.calories_from_carbs/self.calories if self.calories != 0 else 0 #Calories from carbs over total calories
        self.cholesterol_per_calorie = self.cholesterol/self.calories if self.calories !=0 else 0 #Cholesterol per calorie (mg / kcal)
        self.sugar_per_calorie = self.sugar/self.calories if self.calories !=0 else 0 #Sugar per calorie (g / kcal)
        self.fiber_per_calorie = self.fiber/self.calories if self.calories !=0 else 0 #Fiber per calorie (g / kcal)
        self.sodium_per_calorie = self.sodium/self.calories if self.calories !=0 else 0 #Sodium per calorie (mg /kcal)
        self.sugar_per_floz = self.sugar / self.floz if self.type_of_item == 'drink' else 0 #Sugar per fluid ounce (g / fl oz) if item is a drink

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name