from django.shortcuts import render
from django.core import serializers
from . import models
import json

def index(request):
  ingredients = models.Ingredient.objects.all()
  context = {
    'ingredients': ingredients,
  }
  return render(request, 'life/index.html', context)

# def ingredients(request):
#  response = serialize('json',all_groups)
#  return HttpResponse(response, content_type='application/json')