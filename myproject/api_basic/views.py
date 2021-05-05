from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import NBAplayers
from .serializers import NBAplayersSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
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
@csrf_exempt
def player_detail(request,pk):
	try:
		player = NBAplayers.objects.get(pk=pk)

	except NBAplayers.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = NBAplayersSerializer(player)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = NBAplayersSerializer(player, data=data)
		if serializer.isvalid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		player.delete()
		return HttpResponse(status = 204)