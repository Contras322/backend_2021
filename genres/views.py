from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from genres.models import Genre
from genres.serializer import GenreSerializer
from application.views import user_id_auth


class GenreViewSet(viewsets.ViewSet):
    @user_id_auth
    def list(self, request):
        queryset = Genre.objects.all()
        serializer = GenreSerializer(queryset, many=True)

        return Response(serializer.data)

    @user_id_auth
    def retrieve(self, request, pk=None):
        queryset = Genre.objects.all()
        genre = get_object_or_404(queryset, pk=pk)
        serializer = GenreSerializer(genre)

        return Response(serializer.data)

    @user_id_auth
    def create(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            genre = serializer.create(validated_data=request.data)
            serializer = GenreSerializer(genre)

            return Response({"status": "success", "data": serializer.data, "message": None})
        else:
            return Response(serializer.errors)

    @user_id_auth
    def update(self, request, pk=None):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            Genre.objects.filter(pk=pk).update(**self.request.data)

            return Response({"data": serializer.data})

        return Response({"errors": serializer.errors})

    @user_id_auth
    def delete(self, request, pk=None):
        genre = get_object_or_404(Genre.objects.all(), pk=pk)
        genre.delete()

        return Response({"status": "success", "message": None})
