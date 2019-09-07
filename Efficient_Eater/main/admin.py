from django.contrib import admin
from .models import Restaurant, Item
# Register your models here.

class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name and Logo", {"fields": ["name","logo"]}),
        ("Description", {"fields": ["description"]})
    ]

class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Restaurant and Name", {"fields": ["restaurant", "name"]}),
        ("Type of Item (and fluid volume)", {"fields": ["type_of_item", "floz"]}),
        ("Calories", {"fields": ["calories"]}),
        ("Total Fat", {"fields": ["total_fat", "sat_fat","trans_fat"]}),
        ("Cholesterol", {"fields": ["cholesterol"]}),
        ("Sodium", {"fields": ["sodium"]}),
        ("Total Carbohydrates", {"fields": ["carbs", "fiber", "sugar"]}),
        ("Protein", {"fields": ["protein"]})
    ]

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Item, ItemAdmin)
