from .views import (
    WatchListAV,
    WatchDetailAV,
    StreamPlatformAV,
    StreamPlatformDetailAV,
    ReviewList,
    ReviewDetail,
)

# from watchlist_app.views import movie_list, movie_detail

from django.urls import path

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie_list"),
    path("<int:pk>", WatchDetailAV.as_view(), name="movie_detail"),
    path("stream/", StreamPlatformAV.as_view(), name="stream"),
    path("stream/<int:pk>", StreamPlatformDetailAV.as_view(), name="stream"),
    path("stream/1/review", StreamPlatformAV.as_view(), name="stream"),
    path("stream/1/review/<int:pk>", StreamPlatformAV.as_view(), name="stream"),
    path("review", ReviewList.as_view(), name="review_list"),
    path("review/<int:pk>", ReviewDetail.as_view(), name="review_detail"),
]
