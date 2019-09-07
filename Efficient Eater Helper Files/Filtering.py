from Fast_Food_Object import *

def sortByMetric(listOfItems, metric='calories', descending=False):
    newlist = sorted(listOfItems,key=lambda x: getattr(x, metric), reverse=descending)
    return newlist

#Make sure to exclude food that is 5 calories or under when calculating efficiences to avoid inaccuracies or Iced Tea Large at McDoanlds comes out to 80% protein efficient
def test():
    new_item1 = Menu_Item_Without_Price(name='Bacon Buffalo Ranch McChicken',
                         restaurant='McDonalds',
                         type_of_item='food',
                         calories=440,
                         protein=20,
                         carbs=41,
                         fat=23)

    new_item2 = Menu_Item_Without_Price(name='The Zarbail',
                         restaurant='McDonalds',
                         type_of_item='food',
                         calories=420,
                         protein=70,
                         carbs=40,
                         fat=21)

    new_item3 = Menu_Item_Without_Price(name='Agasi',
                         restaurant='McDonalds',
                         type_of_item='drink',
                         calories=4200,
                         protein=690,
                         carbs=420,
                         fat=100)

    listOfItems = []
    listOfItems.append(new_item1)
    listOfItems.append(new_item2)
    listOfItems.append(new_item3)

    print(sortByMetric(listOfItems))
    print(sortByMetric(listOfItems, metric='carbs'))
    print(sortByMetric(listOfItems, metric='protein_efficiency'))