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
		Occident 	= 'West Region'
		Center		= 'Region Central'
		Orient		= 'East Region'

	class OptionsType(models.TextChoices):
		unknown			= 'unknown'
		Metalífero		= 'metalífero'
		Nometalífero	= 'nometalífero'
	
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

class Proyects(models.Model):
	name		= models.CharField(max_length=50,blank=False, default='unknown')
	Firma		= models.CharField(max_length=50,blank=False, default='unknown')
	Group		= models.TextField(blank=True, default='unknown')
	main_res	= models.CharField(max_length=20,blank=None, default='Copper')
	region 		= models.TextField(blank=True, default='Around there')
	life_cycle	= models.FloatField()


class Region(models.Model):

	class ClimateOptions(models.TextChoices):
		unknown		= 'unknown'
		Arid 		= 'Arido'
		Dry			= 'Seco'
		Humid		= 'Humedo'

	class Embossments(models.TextChoices):
		unknown		= 'unknown'
		Plain		= 'llano'
		Mountain	= 'Montañoso'
		Desert		= 'Desierto'


	climate		= models.CharField(	max_length=50,
									choices=ClimateOptions.choices, 
									default='unknown')
	altitude	= models.FloatField()
	embossment	= models.CharField(	max_length=50,
									choices=Embossments.choices, 
									default='unknown')