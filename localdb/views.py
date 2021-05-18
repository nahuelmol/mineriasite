from django.shortcuts import render
from django.views import View

class Homepage(View):

	def get(self,request):
		context = {'data':'data_example'}
		return render(request,'db/homepage.html',context)

class MinersImportance(View):
	def get(self,request):
		context = {'data':'example'}
		return render(request,'db/mine_important.html',context)

class MinersHistory(View):
	def get(self,request):
		context = {'some':'somedata'}
		return render(request,'db/history.html',context)

class MinersStore(View):
	def get(self,request):
		context = {'ex':'example'}
		return render(request,'db/info_db.html',context)