from django import template

register = template.Library()
@register.filter
def filter(listOfItems, metric, reverse=True):
    newlist = sorted(listOfItems, key=lambda x: getattr(x, metric), reverse=reverse)
    return newlist
