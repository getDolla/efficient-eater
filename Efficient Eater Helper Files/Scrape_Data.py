from bs4 import BeautifulSoup as bs
from Filtering import sortByMetric
import requests
from Fast_Food_Object import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
import random
import sys
import platform
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
if platform.system().lower() == 'windows' or platform.system().lower() == 'win32':
    OS = 'Windows'
elif platform.system().lower() == 'darwin':
    OS = 'Mac'

POPULAR_MENU_ITEMS_URL = "https://www.menuwithprice.com/menu-and-price/"
MENU_SITE_URL = "https://www.menuwithprice.com/nutrition/"
NUTRITION_SITE_URL = "https://www.fastfoodmenuprices.com/"

def init_driver():
    # initiate the driver:
    if OS == "Windows":
        driver = webdriver.Chrome('D:\Coding Stuff\chromedriver.exe')
    elif OS == "Mac":
        driver = webdriver.Chrome(executable_path=current_dir+'/chromedriver')
    # set a default wait time for the browser [3 seconds here]:
    driver.wait = WebDriverWait(driver, 3)
    return driver

def close_driver(driver):
    driver.close()

def getRestaurantsFromFile(textfile):
    with open(textfile) as file:
        restaurants = []
        line = file.readline()
        while line:
            locations.append(line.strip())
            line = file.readline()
        return restaurants

def getMenuItemsFromRestaurantBACKUP(restaurant):
    mod_restaurant = restaurant.replace("'", "") #Remove apostrophes from URL
    mod_restaurant = mod_restaurant.replace(" ","-") #Remove spaces and replace them with hyphens for URL
    page_source = requests.get(NUTRITION_SITE_URL+mod_restaurant+"-nutrition/").content
    soup = bs(page_source, "lxml")
    metrics = []
    for metric in soup.find_all('th'):
        if "total fat" in metric.text.lower():
            metric_name = "fat"
        elif 'sugars' in metric.text.lower():
            metric_name = "sugar"
        elif 'size' in metric.text.lower():
            metric_name = "size"
        else: metric_name = metric.text.lower().strip()
        metrics.append(metric_name)

    items = []
    table = soup.find('tbody')
    previous_name = None
    for row in table.find_all('tr'):
        tds = row.find_all('td')
        if len(tds) == 1 or len(tds) == 2: #Check to see if the row is the name of the category of item
            type_of_item = row.find('h3').text.lower()
            if 'drink' in type_of_item or 'beverage' in type_of_item:
                type_of_item = 'drink'
            elif 'dessert' in type_of_item:
                type_of_item = 'dessert'
            elif 'additional options' in type_of_item:
                type_of_item = 'additional options'
            else: type_of_item = 'meal'
        else:
            for counter, td in enumerate(tds):
                if metrics[counter] == 'food':
                    if td.text == '': name = previous_name
                    else:
                        name = td.text.replace('®', '').lower()
                        name = name.replace('()', '')
                        name = name.replace('‡', '')
                        name = name.strip()
                    previous_name = name
                elif metrics[counter] == 'size':
                    if td.text !='': name = name + f' ({td.text.lower()})'
                elif metrics[counter] == 'calories':
                    temp = td.text.strip()
                    temp = temp.replace(",", "")
                    if '-' in temp or '<' in temp: calories = 0
                    elif temp == '' or temp == 'N/A': continue
                    else: calories = int(temp)
                elif metrics[counter] == 'fat':
                    temp = td.text.strip(' ')
                    temp = temp.replace('g', '')
                    temp = temp.strip('m')
                    if '<' in temp or '-' in temp: fat = 0
                    elif temp == '' or temp == 'N/A': continue
                    elif '.' in temp: fat = float(temp)
                    else: fat = int(temp)
                elif metrics[counter] == 'carbs':
                    temp = td.text.strip(' ')
                    temp = temp.replace('g', '')
                    temp = temp.strip('m')
                    if '<' in temp or '-' in temp: carbs = 0
                    elif temp == '' or temp == 'N/A': continue
                    elif '.' in temp: carbs = float(temp)
                    else: carbs = int(temp)
                elif metrics[counter] == 'protein':
                    temp = td.text.strip(' ')
                    temp = temp.replace('g', '')
                    temp = temp.strip('m')
                    if '<' in temp or '-' in temp: protein = 0
                    elif temp == '' or temp == 'N/A': continue
                    elif '.' in temp: protein = float(temp)
                    else: protein = int(temp)

            item = Menu_Item_Simple_Without_Price(name=name,
                            restaurant=restaurant,
                            type_of_item=type_of_item,
                             calories = calories,
                             protein = protein,
                             carbs = carbs,
                             fat = fat)
            items.append(item)

    return items

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
        print(dd.text)
        if 'fl oz' in dd.text:
            floz = int(dd.text.split(' ')[-3])
            type_of_item = 'drink'
        for metric in dd.find_all('li'):
            if "Calories " in metric.text:
                calories = int(metric.text.split(' ')[-1])
            elif "Total Fat" in metric.text:
                total_fat = float(metric.text.split(' ')[-1].strip('g'))
            elif "Saturated Fat" in metric.text:
                sat_fat = float(metric.text.split(' ')[-1].strip('g'))
            elif "Trans Fat" in metric.text:
                trans_fat = float(metric.text.split(' ')[-1].strip('g'))
            elif "Cholesterol" in metric.text:
                cholesterol = float(metric.text.split(' ')[-1].strip('mg'))
            elif "Sodium" in metric.text:
                sodium = float(metric.text.split(' ')[-1].strip('mg'))
            elif "Carbohydrates" in metric.text:
                carbs = float(metric.text.split(' ')[-1].strip('g'))
            elif "Fiber" in metric.text:
                fiber = float(metric.text.split(' ')[-1].strip('g'))
            elif "Sugar" in metric.text:
                sugar = float(metric.text.split(' ')[-1].strip('g'))
            elif "Protein" in metric.text:
                protein = float(metric.text.split(' ')[-1].strip('g'))
    item = Menu_Item_Extended_Without_Price(name=name,
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
                                            floz=floz if type_of_item == 'drink' else None)
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
    return item

def main():
    menu = []
    '''
    with open('Restaurants', 'r') as file:
        line = file.readline()
        while line:
            restaurant = line.strip()
            print(f"Gathering items from {restaurant}")
            menu.extend(getMenuItemsFromRestaurant(restaurant))
            line = file.readline()
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

if __name__ == "__main__":
    main()