from django.contrib import admin
from django.urls import path
from .views import players_list, player_detail

urlpatterns = [
    path('players/', players_list),
    path('detail/<int:pk>/', player_detail)

]
