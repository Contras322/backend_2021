from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from genres.models import Genre
from genres.serializer import GenreSerializer


class GenreViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Genre.objects.all()
        serializer = GenreSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Genre.objects.all()
        genre = get_object_or_404(queryset, pk=pk)
        serializer = GenreSerializer(genre)

        return Response(serializer.data)

    def create(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            genre = serializer.create(validated_data=request.data)
            serializer = GenreSerializer(genre)

            return Response({"status": "success", "data": serializer.data, "message": None})
        else:
            return Response(serializer.errors)

    def update(self, request, pk=None):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            Genre.objects.filter(pk=pk).update(**self.request.data)

            return Response({"data": serializer.data})

        return Response({"errors": serializer.errors})

    def delete(self, request, pk=None):
        genre = get_object_or_404(Genre.objects.all(), pk=pk)
        genre.delete()

        return Response({"status": "success", "message": None})
