from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
	title = models.CharField(max_length=100)
	release_year = models.IntegerField()


class Rating(models.Model):
	user = models.ForeignKey(User, models.CASCADE)
	movie = models.ForeignKey(Movie, models.CASCADE)
	rating = models.IntegerField(
			default=-1,
			validators=[MaxValueValidator(10), MinValueValidator(-1)]
		)
