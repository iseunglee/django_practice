from django.contrib import admin
from kiosk.models import DrinkType

@admin.register(DrinkType)
class DrinkTypeAdmin(admin.ModelAdmin):
    list_play = ('type_name', 'add_date')
