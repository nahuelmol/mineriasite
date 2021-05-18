from localdb.models import Interprise, Mineral, Proyects
from localdb.api.serializer import InterpriseSerializer, MineralSerializer
from localdb.api.serializer import ProyectsSerializer, RegionsSerializer

from rest_framework.response import Response
from rest_framework import viewsets

from django.shortcuts import render

class InterprisesView(viewsets.ViewSet):
    @staticmethod
    def list(self):
        queryset        = Interprise.objects.all()
        serialized      = InterpriseSerializer(queryset, many=True)
        return Response(serialized.data) 

class MineralsView(viewsets.ViewSet):
	@staticmethod
	def list(self):
		queryset		= Mineral.objects.all()
		serialized		= MineralSerializer(queryset, many=True)
		return Response(serialized.data)

class ProyectsView(viewsets.ViewSet):
	@staticmethod
	def list(self):
		queryset		= Proyects.objects.all()
		serialized		= ProyectsSerializer(queryset,many=True)
		return Response(serialized.data)

class RegionsView(viewsets.ViewSet):
	@staticmethod
	def list(self):
		queryset		= Region.objects.all()
		serialized		= RegionsSerializer(queryset,many=True)
		return Response(serialized.data)