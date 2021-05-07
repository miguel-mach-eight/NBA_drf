from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import NBAplayers
from .serializers import NBAplayersSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions


class NBAPlayersViewSet(viewsets.ModelViewSet):
	serializer_class = NBAplayersSerializer
	queryset = NBAplayers.objects.all()


# Create your views here.
