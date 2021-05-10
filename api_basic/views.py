from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import NBAplayers, User
from .serializers import NBAplayersSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

class ReadOnlyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        requests = ('POST', 'PUT', 'DELETE', 'PATCH')
        user = request.user
        if user.is_anonymous:  # Not Authenticated
            return request.method == 'GET'            
        else:    
            if user.role == 'read-write':
                return request.method in requests + ('GET',)
            else:  # Read Only User
                return request.method == 'GET'

class NBAPlayersViewSet(viewsets.ModelViewSet):
	serializer_class = NBAplayersSerializer
	queryset = NBAplayers.objects.all()
	permission_classes = [ReadOnlyPermission]