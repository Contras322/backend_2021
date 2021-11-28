from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'genre', 'rating']

    def create(self, validated_data):
        data = {
            'id': validated_data['id'],
            'name': validated_data['name'],
            'genre': Genre.objects.get(id=validated_data['genre']),
            'rating': validated_data['rating'],
        }

        return Movie.objects.create(**data)
