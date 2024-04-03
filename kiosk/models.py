from django.db import models

class DrinkType(models.Model):
    type_name = models.CharField(max_length=100)
    add_date = models.DateTimeField("add date")

class Menu(models.Model):
    drink_type = models.ForeignKey(DrinkType, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)