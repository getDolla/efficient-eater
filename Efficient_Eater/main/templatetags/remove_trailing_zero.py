from django import template
from decimal import *
register = template.Library()
@register.filter
def remove_trailing_zero(value):
    return int(value) if ".0" in str(value) else value