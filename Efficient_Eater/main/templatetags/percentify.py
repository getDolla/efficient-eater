from django import template
from decimal import *
register = template.Library()
@register.filter
def percentify(value):
    return round(Decimal(value*100),1)