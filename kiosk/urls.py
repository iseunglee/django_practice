from django.urls import path
from . import views

app_name = 'kiosk'

urlpatterns = [
    path("", views.DrinkTypeLV.as_view(), name='index'),

]