from django.shortcuts import render, redirect
from .models import Restaurant, Item

# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name="main/home.html",
                  context={"restaurants": Restaurant.objects.all,
                           "items": Item.objects.all})

#"items": Item.objects.all().exclude(calories__lte=500).order_by('protein')