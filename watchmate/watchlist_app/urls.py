from watchlist_app.views import movie_list
from django.urls import path

urlpatterns = [path("list/", movie_list, name="movie_list")]
