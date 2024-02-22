from watchlist_app.models import Watchlist, StreamPlatform, Review
from watchlist_app.api.serializers import (
    Watchlistserilizer,
    StreamPlatformSerializer,
    ReviewSerializer,
)
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from watchlist_app.api.permissions import AdminOrReadOnly,IsReviewUserOrReadOnly
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        movie = Watchlist.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(
            watchlist=movie, review_user=review_user
        )
        if review_queryset.exists():
            raise ValidationError({"error": "You already have a review for this movie"})
        if movie.number_rating ==0:
            movie.avg_rating = serializer.validated_data["rating"]
        else:
            movie.avg_rating = (movie.avg_rating+serializer.validated_data["rating"])/2
        movie.number_rating=movie.number_rating+1
        movie.save()
        
        serializer.save(watchlist=movie, review_user=review_user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]
    throttle_classes=[UserRateThrottle,AnonRateThrottle]




class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes=[UserRateThrottle,AnonRateThrottle]


    def get_queryset(self):
        pk = self.kwargs["pk"]
        return Review.objects.filter(watchlist=pk)
    

# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ReviewList(
#     mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
# ):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class StreamPlatformAV(APIView):
    def get(self, request):

        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        # serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailAV(APIView):
    permission_classes=[AdminOrReadOnly]

    def get(self, request, pk):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(
                {"Error": "Movie NOt Found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = StreamPlatformSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = StreamPlatform.objects.get(pk=pk)
        movie.delete()
        return Response(status=204)


class WatchListAV(APIView):
    permission_classes=[AdminOrReadOnly]


    def get(self, request):
        movies = Watchlist.objects.all()
        serializer = Watchlistserilizer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Watchlistserilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailAV(APIView):
    permission_classes=[AdminOrReadOnly]
    def get(self, request, pk):
        try:
            movie = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response(
                {"Error": "Movie NOt Found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = Watchlistserilizer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Watchlist.objects.get(pk=pk)
        serializer = Watchlistserilizer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = Watchlist.objects.get(pk=pk)
        movie.delete()
        return Response(status=204)


# @api_view(["GET", "POST"])
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = Watchlistserilizer(movies, many=True)
#         return Response(serializer.data)
#     if request.method == "POST":
#         serializer = Watchlistserilizer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


# @api_view(["GET", "PUT", "DELETE"])
# def movie_detail(request, pk):
#     if request.method == "GET":
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({"Error":"Movie not Found"}, status=status.HTTP_404_NOT_FOUND)

#         serializer = Watchlistserilizer(movie)
#         return Response(serializer.data)
#     if request.method == "PUT":
#         movie = Movie.objects.get(pk=pk)
#         serializer = Watchlistserilizer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     if request.method == "DELETE":
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=204)
