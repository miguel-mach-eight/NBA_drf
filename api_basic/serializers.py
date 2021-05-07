from rest_framework import serializers
from .models import NBAplayers


class NBAplayersSerializer(serializers.ModelSerializer):
	class Meta:
		model = NBAplayers 
		fields = ['id','first_name','h_in','h_meters', 'last_name']