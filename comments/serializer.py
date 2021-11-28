from rest_framework import serializers
from comments.models import Comment
from movies.models import Movie


class CommentSerializer(serializers.ModelSerializer):
    movie = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author_name', 'text', 'movie']

    def create(self, validated_data):
        data = {
            'id': validated_data['id'],
            'author_name': validated_data['author_name'],
            'text': validated_data['text'],
            'movie': Movie.objects.get(name=validated_data['movie']),
        }

        return Comment.objects.create(**data)