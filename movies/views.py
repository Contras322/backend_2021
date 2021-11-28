from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from movies.models import Movie
from movies.serializer import MovieSerializer


class MovieViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Movie.objects.all()
        movie = get_object_or_404(queryset, pk=pk)
        serializer = MovieSerializer(movie)

        return Response(serializer.data)

    def create(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            movie = serializer.create(validated_data=request.data)
            serializer = MovieSerializer(movie)

            return Response({"status": "success", "data": serializer.data, "message": None})
        else:
            return Response(serializer.errors)

    def update(self, request, pk=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            Movie.objects.filter(pk=pk).update(**self.request.data)

            return Response({"data": serializer.data})

        return Response({"errors": serializer.errors})

    def delete(self, request, pk=None):
        movie = get_object_or_404(Movie.objects.all(), pk=pk)
        movie.delete()

        return Response({"status": "success", "message": None})
