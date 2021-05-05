from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import NBAplayers
from .serializers import NBAplayersSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def players_list(request):
	if request.method == 'GET':
		players = NBAplayers.objects.all()
		serializer = NBAplayersSerializer(players, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		
		serializer = NBAplayersSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
@api_view(['GET','PUT','DELETE'])
def player_detail(request,pk):
	try:
		player = NBAplayers.objects.get(pk=pk)

	except NBAplayers.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = NBAplayersSerializer(player)
		return Response(serializer.data)

	elif request.method == 'PUT':
		
		serializer = NBAplayersSerializer(player, data=request.	data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		player.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)