from Fast_Food_Object import Menu_Item

def sortByMetric(listOfItems, metric='calories', descending=False):
    newlist = sorted(listOfItems,key=lambda x: getattr(x, metric), reverse = descending)
    return newlist

new_item1 = Menu_Item(name='Bacon Buffalo Ranch McChicken',
                     restaurant='McDonalds',
                     type_of_item='food',
                     calories=440,
                     protein=20,
                     carbs=41,
                     fat=23,
                     price=5.00)

new_item2 = Menu_Item(name='The Zarbail',
                     restaurant='McDonalds',
                     type_of_item='food',
                     calories=420,
                     protein=70,
                     carbs=40,
                     fat=21,
                     price=69.00)

new_item3 = Menu_Item(name='Agasi',
                     restaurant='McDonalds',
                     type_of_item='drink',
                     calories=4200,
                     protein=690,
                     carbs=420,
                     fat=100,
                     price=690.00)

listOfItems = []
listOfItems.append(new_item1)
listOfItems.append(new_item2)
listOfItems.append(new_item3)

print(sortByMetric(listOfItems))
print(sortByMetric(listOfItems, metric='carbs'))
print(sortByMetric(listOfItems, metric='price', descending=True))
print(sortByMetric(listOfItems, metric='protein_efficiency'))