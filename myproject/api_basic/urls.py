from django.contrib import admin
from django.urls import path, include
from .views import  NBAPlayersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('players', NBAPlayersViewSet, basename = 'Players list')


urlpatterns = [
	path('viewset/', include(router.urls)),
	path('viewset/<int:pk/', include(router.urls)),
]
