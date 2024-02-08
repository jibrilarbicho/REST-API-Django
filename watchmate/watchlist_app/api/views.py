from watchlist_app.models import Movie
from watchlist_app.api.serializers import Movieserilizer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = Movieserilizer(movies, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = Movieserilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def movie_detail(request, pk):
    if request.method == "GET":
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"Error:Movie not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Movieserilizer(movie)
        return Response(serializer.data)
    if request.method == "PUT":
        movie = Movie.objects.get(pk=pk)
        serializer = Movieserilizer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == "DELETE":
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=204)
