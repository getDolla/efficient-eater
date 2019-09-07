from .models import Item

def sortByMetric(listOfItems, metric='calories', descending=True):
    newlist = sorted(listOfItems,key=lambda x: getattr(x, metric), reverse=descending)
    return newlist

#Make sure to exclude food that is 5 calories or under when calculating efficiences to avoid inaccuracies or Iced Tea Large at McDoanlds comes out to 80% protein efficient
