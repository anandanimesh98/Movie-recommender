from django.contrib import admin
from .models import Rating, Movie

admin.site.register(Movie)
admin.site.register(Rating)
# Register your models here.
