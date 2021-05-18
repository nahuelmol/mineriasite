from django.shortcuts import render
from django.views import View

class Homepage(View):

	def get(self,request):
		context = {'data':'data_example'}
		return render(request,'db/homepage.html',context)

