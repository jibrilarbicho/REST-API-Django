from .views import (
    WatchListAV,
    WatchDetailAV,
    StreamPlatformAV,
    StreamPlatformDetailAV,
    ReviewList,
    ReviewDetail,
    ReviewCreate,UserReview,
    Watchlist
)

# from watchlist_app.views import movie_list, movie_detail

from django.urls import path

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="movie_list"),
    path("<int:pk>", WatchDetailAV.as_view(), name="movie_detail"),
    path("list2/", Watchlist.as_view(), name="watchList"),

    path("stream/", StreamPlatformAV.as_view(), name="stream"),
    path("stream/<int:pk>", StreamPlatformDetailAV.as_view(), name="stream"),
    path("stream/<int:pk>/review/", ReviewList.as_view(), name="review_list"),
    path("stream/<int:pk>/review_create", ReviewCreate.as_view(), name="review_create"),
    path("stream/review/<int:pk>", ReviewDetail.as_view(), name="review_detail"),
    # path("stream/review/<str:username>", UserReview.as_view(), name="user_review"),
    path("stream/review/", UserReview.as_view(), name="user_review"),

    # path("review", ReviewList.as_view(), name="review_list"),
    # path("review/<int:pk>", ReviewDetail.as_view(), name="review_detail"),
]
