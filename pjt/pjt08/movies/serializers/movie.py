from rest_framework import serializers
from ..models import Movie, Review, Actor

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title',)


class MovieSerializer(serializers.ModelSerializer):

    class ActorSerilizer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('id', 'name',)

    class ReviewSerilizer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('id', 'title',)
    
    title = serializers.CharField(min_length=1, max_length=100)
    actors = ActorSerilizer(many=True, read_only=True)
    reviews = ReviewSerilizer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'release_date', 'actors', 'reviews', 'poster_path',)