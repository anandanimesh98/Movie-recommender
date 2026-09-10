#Contains set of all callback functions to execute

from django.http import HttpResponse
from django.shortcuts import redirect, render


def home_page(req):
	# the landing page is the login form; signed in users go straight to
	# their recommendations instead of being shown it again
	if req.user.is_authenticated:
		return redirect('/recommender/' + req.user.username + '/')
	return redirect('accounts:login')

