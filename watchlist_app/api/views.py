from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from watchlist_app.api.serializers import MovieSerializer
from watchlist_app.models import Movie

# by default @api_view is set to 'GET'
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        #We use many=True when we want to access all objects
        serializer = MovieSerializer(movies, many=True)
        #To access all objects we use 'serializer.data'
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

'''
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "name": "Python vs. Java",
        "description": "Description 1",
        "active": true
    },
    {
        "id": 2,
        "name": "JavaScript - The Face",
        "description": "Description 2",
        "active": true
    }
]

'''

# Put(update all data) vs. Patch(update only a signle field - a partial update)
@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    if request.method == 'GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors)
    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
