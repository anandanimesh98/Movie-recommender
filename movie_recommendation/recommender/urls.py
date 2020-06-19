from django.urls import path
from . import views

app_name = 'recommender'

urlpatterns = [
	
	path('<str:uname>/', views.display_movies, name="display_movies"),

]