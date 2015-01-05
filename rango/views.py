from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage' : 'I am the bold message we were talking about'}
	return render(request, 'rango/index.html', context_dict)

def about(request):
	html = """
				Rango Says Here is the about page!
				<br>
				<a href="/rango/">Home Page</a>
			"""
	return HttpResponse(html)
