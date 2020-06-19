#Contains set of all callback functions to execute

from django.http import HttpResponse
from django.shortcuts import render


def home_page(req):
	#return HttpResponse('home page')
	if req.method == 'POST':
		print(req.POST)
	return render(req, 'homepage.html')

