from rest_framework import serializers
from localdb.models import Interprise, Mineral, Proyects

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