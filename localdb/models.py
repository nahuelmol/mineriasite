from django.db import models

class Interprise(models.Model):
	name				= models.TextField(max_length=50)
	origin				= models.CharField(max_length=20)
	foreign_operator	= models.TextField(max_length=50)
	local_operator		= models.TextField(max_length=50)
	website				= models.CharField(	max_length=20,
											blank=None,
											default='NotWebsiteForThisOne')

class Mineral(models.Model):
	class OptionsRegion(models.TextChoices):
		unknown		= 'unknown'
		Occidente 	= 'Region Occidental'
		Centro		= 'Region Central'
		Oriente		= 'Region Oriental'

	class OptionsType(models.TextChoices):
		unknown			= 'unknown'
		metalífero		= 'metalífero'
		nometalífero	= 'nometalífero'
	
	name				= models.CharField(max_length=20)
	typeof				= models.CharField(	max_length=15,
											choices=OptionsType.choices,
											default='unknown')
	proyect				= models.TextField(max_length=40)
	rocadeaplicación	= models.BooleanField(blank=None,default=False)
	metalprecioso		= models.BooleanField(blank=None,default=False)
	region				= models.TextField(	max_length=40,
											choices=OptionsRegion.choices,
											blank=None,
											default='unknown')