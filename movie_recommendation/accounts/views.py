from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def signup_view(req):
	if req.method == 'POST':
		form = UserCreationForm(req.POST)
		if form.is_valid():
			user = form.save()
			# log the user in
			login(req, user)
			print(req.user)
			print("123")
			return redirect('/recommender/' + req.user.username+'/')
	else:
		form = UserCreationForm()
		
	return render(req, 'accounts/signup.html', {'form': form})


def login_view(req):
	if req.method == 'POST':
		form = AuthenticationForm(data=req.POST)
		if form.is_valid():
			# login the user
			user = form.get_user()
			login(req, user)
			if 'next' in req.POST:
				return redirect(req.POST.get('next'))
			else:
				return redirect('/recommender/' + req.user.username+'/')

	else:
		form = AuthenticationForm()

	# req.GET.get('next') is used to get the next part of query string 
	return render(req, 'accounts/login.html', {'form': form, 'nxt': req.GET.get('next')})


def logout_view(req):
	if req.method == 'POST':
		logout(req)
		return redirect('/')
 