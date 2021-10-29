from rest_framework import serializers
from ..models import Movie, Review, Actor

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'title',)


class ReviewSerializer(serializers.ModelSerializer):

    class MovieSerilizer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title',)
    
    title = serializers.CharField(min_length=1, max_length=100)
    movies = MovieSerilizer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movies',)