from .views import MovieListAV, MovieDetailAV

# from watchlist_app.views import movie_list, movie_detail

from django.urls import path

urlpatterns = [
    path("list/", MovieListAV.as_view(), name="movie_list"),
    path("<int:pk>", MovieDetailAV.as_view(), name="movie_detail"),
]
