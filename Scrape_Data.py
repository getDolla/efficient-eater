from Fast_Food_Object import Menu_Item
from bs4 import BeautifulSoup as bs
import requests
import time
import random
import sys
import platform
import os

POPULAR_MENU_ITEMS_URL = "https://www.menuwithprice.com/menu-and-price/"
MENU_SITE_URL = "https://www.menuwithprice.com/menu/"
NUTRITION_SITE_URL = "https://www.fastfoodmenuprices.com/"
def getRestaurantsFromFile(textfile):
    with open(textfile) as file:
        restaurants = []
        line = file.readline()
        while line:
            locations.append(line.strip())
            line = file.readline()
        return restaurants

def getMenuItemsFromRestaurant(restaurant):
    mod_restaurant = restaurant.replace("'", "") #Remove apostrophes from URL
    mod_restaurant = restaurant.replace(" ","-") #Remove spaces and replace them with hyphens for URL
    page_source = requests.get(NUTRITION_SITE_URL+mod_restaurant+"-nutrition/").content
    soup = bs(page_source, "lxml")
    thread = soup.find('thread')
    metrics = []
    for metric in thread.find_all('th'):
        if "total fat" in metric.text.lower():
            metric_name = "fat"
        else: metric_name = metric.text.lower().strip()
        metrics.append((counter, metric_name))
    items = []
    for table in soup.find('tbody'):
        previous_name = None
        for row in table.find_all('tr'):
            item = Menu_Item()
            tds = row.find_all('td')
            if len(tds) == 1:
                type_of_item = row.find('h3').text.lower()
                if 'drink' in type_of_item:
                    type_of_item = 'drink'
                else: type_of_item = 'meal'
            else:
                for counter, td in enumerate(tds):
                    if metrics[counter] == 'food':
                        if td.text == '':
                            name = previous_name
                        name = td.text.replace('®', '').lower()
                        item.name = name
                        previous_name = name
                    elif metrics[counter] == 'size':
                        item.name = item.name + f' ({td.text})'
                    elif metrics[counter] == 'calories':
                        item.calories = int(td.text.strip())
                    elif metrics[counter] == 'fat':
                        item.calories = int(td.text.strip())
                    elif metrics[counter] == 'carbs':
                        item.carbs = int(td.text.strip())
                    elif metrics[counter] == 'protein':
                        item.protein = int(td.text.strip())
                    item.restaurant = restaurant
                    item.type_of_item = type_of_item
                print(item.name)
                print(item.restaurant)
                print(item.type_of_item)
                print(item.calories)
                print(item.fat)
                print(item.carbs)
                print(item.protein)
                items.append(item)






getMenuItemsFromRestaurant("Burger King")