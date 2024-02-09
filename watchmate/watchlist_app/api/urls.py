from .views import WatchListAV, WatchDetailAV, StreamPlatformAV

# from watchlist_app.views import movie_list, movie_detail

from django.urls import path

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie_list"),
    path("<int:pk>", WatchDetailAV.as_view(), name="movie_detail"),
    path("stream/", StreamPlatformAV.as_view(), name="stream"),
]
