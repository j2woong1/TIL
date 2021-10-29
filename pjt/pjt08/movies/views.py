from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Actor, Movie, Review

from .serializers.actor import ActorListSerializer, ActorSerializer
from .serializers.movie import MovieListSerializer, MovieSerializer
from .serializers.review import ReviewListSerializer, ReviewSerializer


@api_view(['GET', 'POST'])
def actor_list_or_create(request):
    
    def actor_list():
        actors = Actor.objects.all()
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)

    def actor_create():
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    if request.method == 'GET':
        return actor_list()
    elif request.method == 'POST':
        return actor_create()


@api_view(['GET', 'PUT', 'DELETE'])
def actor_detail_or_update_or_delete(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)

    def actor_detail():
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    def actor_update():
        serializer = ActorSerializer(instance=actor, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def actor_delete():
        actor.delete()
        return Response(data='delete successfully', status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return actor_detail()
    elif request.method == 'PUT':
        return actor_update()
    elif request.method == 'DELETE':
        return actor_delete()


@api_view(['GET', 'POST'])
def movie_list_or_create(request):

    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_or_update_or_delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(instance=movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(data='delete successfully', status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def review_create(request, movie_pk):
    movie_id = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie_id)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_or_update_or_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    def review_detail():
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def review_update():
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)
    
    def review_delete():
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return review_detail()
    elif request.method == 'PUT':
        return review_update()
    else:
        return review_delete()