from rest_framework import serializers
from ..models import Movie, Review, Actor

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name',)


class ActorSerializer(serializers.ModelSerializer):

    class MovieSerilizer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title',)

    
    name = serializers.CharField(min_length=2, max_length=100)
    movies = MovieSerilizer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies',)