from watchlist_app.models import Movie
from watchlist_app.api.serializers import Movieserilizer
from rest_framework.response import Response

# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status


class MovieListAV(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = Movieserilizer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Movieserilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(
                {"Error": "Movie NOt Found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = Movieserilizer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = Movieserilizer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=204)


# @api_view(["GET", "POST"])
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serializer = Movieserilizer(movies, many=True)
#         return Response(serializer.data)
#     if request.method == "POST":
#         serializer = Movieserilizer(data=request.data)
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

#         serializer = Movieserilizer(movie)
#         return Response(serializer.data)
#     if request.method == "PUT":
#         movie = Movie.objects.get(pk=pk)
#         serializer = Movieserilizer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     if request.method == "DELETE":
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=204)
