from django.urls import path
from .views import *

urlpatterns = [
    path('', drinkview.as_view(), name='drinks_view'),
    path('<str:id>', UpdateDrinkView.as_view(), name='update_drink_view')
]