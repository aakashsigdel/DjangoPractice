from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage' : 'I am the bold message we were talking about'}
	return render(request, 'rango/index.html', context_dict)

def about(request):
	context_dict = {'funtext' : 'This is very funny to check out'}
	return render(request, 'rango/about.html', context_dict)
