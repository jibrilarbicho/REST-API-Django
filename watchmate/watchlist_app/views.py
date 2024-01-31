from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse


# Create your views here.
def movie_list(requset):
    movies = Movie.objects.all()
    data = {"movies": list(movies.values())}
    return JsonResponse(data)
