from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import NBAplayers
from .serializers import NBAplayersSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class NBAPlayersViewSet(viewsets.ViewSet):
	def list(self, request):
		players = NBAplayers.objects.all()
		serializer = NBAplayersSerializer(players, many=True)
		return Response(serializer.data)

	def create(self, request):
		serializer = NBAplayersSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	

	def retrieve(self, request, pk=None):
		query_set = NBAplayers.objects.all()
		player = get_object_or_404(query_set, pk=pk)
		serializer = NBAplayersSerializer(player)
		return Response(serializer.data)

	def update(self, request, pk=None):
		player = NBAplayers.objects.get(pk=pk)
		serializer = NBAplayersSerializer(player, data=request.	data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def destroy(self, request, pk=None):
		player = NBAplayers.objects.get(pk=pk)
		player.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)


