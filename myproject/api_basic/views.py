from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import NBAplayers
from .serializers import NBAplayersSerializer


def players_list(request):
	if request.method == 'GET':
		players = NBAplayers.objects.all()
		serializer = NBAplayersSerializer(players, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = NBAplayersSerializer(data=data)

		if serializer.isvalid():
			serializer.save()
			return JsonResponse(serializer.data, status = 201)

		return JsonResponse(serializer.errors, status=400)
# Create your views here.
