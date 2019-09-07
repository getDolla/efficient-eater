from bs4 import BeautifulSoup as bs
import requests
from main.models import Item
from decimal import *
import platform
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
if platform.system().lower() == 'windows' or platform.system().lower() == 'win32':
    OS = 'Windows'
elif platform.system().lower() == 'darwin':
    OS = 'Mac'

MENU_SITE_URL = "https://www.menuwithprice.com/nutrition/"


def getRestaurantsFromFile(textfile):
    with open(textfile) as file:
        restaurants = []
        line = file.readline()
        while line:
            locations.append(line.strip())
            line = file.readline()
    return restaurants

def getMenuItemsFromRestaurant(restaurant):
    mod_restaurant = restaurant.replace("'", "")  # Remove apostrophes from URL
    mod_restaurant = mod_restaurant.replace(" ", "-")  # Remove spaces and replace them with hyphens for URL
    page_index = 1
    page_exists = True
    menu = []
    while page_exists:
            url = f'{MENU_SITE_URL}{mod_restaurant}/p/{page_index}'
            page_source_menu = requests.get(url).content
            soup = bs(page_source_menu, "lxml")
            if len(soup.find_all('tr')) > 0:
                for item in soup.find_all('tr'):
                    try:
                        page_source_item = requests.get(item.find('a')['href']).content
                        item_soup = bs(page_source_item, "lxml")
                        item_object = createItemFromData(item_soup, restaurant)
                        menu.append(item_object)
                    except:
                        pass
            else:
                print(f"Finished compiling Full Menu for {restaurant}")
                page_exists = False
            page_index += 1

    return menu

def createItemFromData(soup, restaurant):
    name = soup.find('dd').text
    name = name.replace('®','')
    name = name.replace('©','')
    type_of_item = 'meal'
    for dd in soup.find_all('dd'):
        if 'fl oz' in dd.text:
            floz = int(dd.text.split(' ')[-3])
            type_of_item = 'drink'
        for metric in dd.find_all('li'):
            if "Calories " in metric.text:
                calories = int(metric.text.split(' ')[-1])
            elif "Total Fat" in metric.text:
                total_fat = Decimal(metric.text.split(' ')[-1].strip('g'))
            elif "Saturated Fat" in metric.text:
                sat_fat = Decimal(metric.text.split(' ')[-1].strip('g'))
            elif "Trans Fat" in metric.text:
                trans_fat = Decimal(metric.text.split(' ')[-1].strip('g'))
            elif "Cholesterol" in metric.text:
                cholesterol = Decimal(metric.text.split(' ')[-1].strip('mg'))
            elif "Sodium" in metric.text:
                sodium = Decimal(metric.text.split(' ')[-1].strip('mg'))
            elif "Carbohydrates" in metric.text:
                carbs = Decimal(metric.text.split(' ')[-1].strip('g'))
            elif "Fiber" in metric.text:
                fiber = Decimal(metric.text.split(' ')[-1].strip('g'))
            elif "Sugar" in metric.text:
                sugar = Decimal(metric.text.split(' ')[-1].strip('g'))
            elif "Protein" in metric.text:
                protein = Decimal(metric.text.split(' ')[-1].strip('g'))
    item = Item(name=name,
                restaurant=restaurant,
                type_of_item=type_of_item,
                calories=calories,
                protein=protein,
                carbs=carbs,
                total_fat=total_fat,
                sat_fat=sat_fat,
                trans_fat=trans_fat,
                cholesterol=cholesterol,
                sodium=sodium,
                sugar=sugar,
                fiber=fiber,
                floz=floz if type_of_item == 'drink' else 0)
    print(f"Name: {item.name}")
    print(f"Restaurant: {item.restaurant}")
    print(f"Type Of Item: {item.type_of_item}")
    print(f"Calories: {item.calories}")
    print(f"Protein: {item.protein}")
    print(f"Carbs: {item.carbs}")
    print(f"Total Fat: {item.total_fat}")
    print(f"Saturated Fat: {item.sat_fat}")
    print(f"Trans Fat: {item.trans_fat}")
    print(f"Cholesterol: {item.cholesterol}")
    print(f"Sodium: {item.sodium}")
    print(f"Sugar: {item.sugar}")
    print(f"Fiber: {item.fiber}")
    print(f"Fl Oz: {item.floz}")
    print('-'*40)
    item.save()
    print("O"*50)
    print("Saved Item to Database")
    print("O"*50)
    return item

def main():
    menu=[]
    with open(os.path.join(current_dir, 'Restaurants'), 'r') as file:
        line = file.readline()
        while line:
            restaurant = line.strip()
            print(f"Gathering items from {restaurant}")
            menu.extend(getMenuItemsFromRestaurant(restaurant))
            line = file.readline()
    print(len(menu))
    '''
    menu.extend(getMenuItemsFromRestaurant("McDonald's"))
    new_menu= (sortByMetric(menu, metric='calories', descending=True))
    for item in new_menu:
        print(item)
        print(item.calories)
    print('-'*50)
    new_menu = (sortByMetric(menu, metric='protein_efficiency', descending=True))
    for item in new_menu:
        print(item)
        print(item.protein_efficiency)
    print('-'*50)
    new_menu = (sortByMetric(menu, metric='sugar_per_floz', descending=True))
    for item in new_menu:
        print(item)
        print(item.sugar_per_floz)
    '''

if __name__ == "__main__":
    main()