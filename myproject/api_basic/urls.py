from django.contrib import admin
from django.urls import path
from .views import players_list

urlpatterns = [
    path('players/', players_list),

]
