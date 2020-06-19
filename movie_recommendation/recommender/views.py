from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .helper import *


class MyMovie:
	def __init__(self, title, release_year, img, rating=None):
		self.title = title
		self.release_year = release_year
		self.img = img
		self.rating = rating

	@staticmethod
	def get_movie_list(uname):
		mlist = []
		rdict = {}
		user_ratings = Rating.objects.filter(user = User.objects.get(username=uname))
		for user_rating in user_ratings:
			rdict[user_rating.movie] = user_rating.rating
		for i, movie in enumerate(Movie.objects.all()):
			curr_rating = -1
			if movie in rdict.keys():
				curr_rating = rdict[movie]
			new_movie = MyMovie(movie.title, movie.release_year, str(i+1)+'.jpeg', curr_rating)
			mlist.append(new_movie)
		return mlist

	def __str__(self):
		return self.title




def call_generate_method():
	Arr = []
	for rating in Rating.objects.all():
		tup = [rating.user.id, rating.movie.id, rating.rating]
		Arr.append(tup)
	generate_data_to_process(Arr, len(User.objects.all()), len(Movie.objects.all()))


def call_model_runner(uname):
	mat = get_recommended_movies()
	print(len(mat))
	print(100*'*')
	user = User.objects.get(username=uname)
	rec_movies = []
	print(user.id)
	print(user)
	for movie_id in mat[user.id-1]:
		movie = Movie.objects.get(id=movie_id)
		new_rec = MyMovie(movie.title, movie.release_year, str(movie.id)+'.jpeg')
		rec_movies.append(new_rec)
	return rec_movies


@login_required(login_url="/accounts/login")
def display_movies(req, uname):
	if uname == req.user.username:
		if req.method == 'GET':
			call_generate_method()
			movies = MyMovie.get_movie_list(uname)
			recommended_movies = call_model_runner(uname)
			print(recommended_movies)
			return render(req, 'recommender/movies.html', {'movies': movies, 'uname': uname, 'recommended_movies': recommended_movies})
		else:
			new_rating = Rating.objects.filter(user = User.objects.get(username=uname), movie = Movie.objects.get(title=req.POST['title']))
			if new_rating:
				new_rating = new_rating[0]
				new_rating.rating = req.POST['rating']
			else:
				new_rating = Rating(user = User.objects.get(username=uname), movie = Movie.objects.get(title=req.POST['title']), rating=req.POST['rating'])
			new_rating.save()
			return redirect('/recommender/' + str(uname))
	else:
		return redirect('/')




