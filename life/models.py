from django.db import models

class Group(models.Model):
	established = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
  
class Menu(models.Model):
  established = models.DateTimeField(auto_now_add=True)
  dishname = models.CharField(max_length=50)
  def __str__(self):
    return self.dishname
  
class Ingredient(models.Model):
  name = models.CharField(max_length=50)
  quantity = models.CharField(max_length=50) 
  def __str__(self):
    return self.name

class Directions(models.Model):
  step = models.IntegerField(default=0)
  detail = models.CharField(max_length=500)
  def __str__(self):
    return "Step " + str(self.step)