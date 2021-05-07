from django.contrib import admin
from django.urls import path, include
from .views import  NBAPlayersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('players', NBAPlayersViewSet, basename = 'Players list')


urlpatterns = [
    #djoser basic authentication
    #Routers URLs
	path('', include(router.urls)),
	path('players/<int:pk>/', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]
