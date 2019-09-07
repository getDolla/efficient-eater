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

class Menu_Item():
    def __init__(self, name=None, restaurant=None, type_of_item=None, calories=None, protein=None, carbs=None, fat=None, price=None):
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
        self.protein_per_dollar = self.protein/self.price
        self.fat_per_dollar = self.fat/self.price
        self.carbs_per_dollar = self.carbs/self.price
        self.price_efficiency = self.calories/self.price #Calories per dollar

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
