from rest_framework import serializers
from localdb.models import Interprise, Mineral, Proyects, Region

class InterpriseSerializer(serializers.ModelSerializer):
	class Meta:
		fields	= '__all__'
		model 	= Interprise

class MineralSerializer(serializers.ModelSerializer):
	class Meta:
		fields	= '__all__'
		model 	= Mineral

class ProyectsSerializer(serializers.ModelSerializer):
	class Meta:
		fields 	= '__all__'
		model 	= Proyects 

class RegionsSerializer(serializers.ModelSerializer):
	class Meta:
		fields	= '__all__'
		model 	= Region