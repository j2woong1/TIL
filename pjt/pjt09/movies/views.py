from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods, require_safe
from .models import Movie, Genre
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import random 

# Create your views here.
@require_safe
@require_GET
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
@require_GET
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
@require_GET
def recommended(request):
    if request.user.is_authenticated:
        favorite_genres = request.user.favorite_genres.all()

        recommended_movies = set()
        for movie in Movie.objects.prefetch_related('genres'):
            if movie.genres.intersection(favorite_genres):
                recommended_movies.add(movie)
                
        context = {
            'recommended_movies': random.sample(recommended_movies, min(10, len(recommended_movies))),
        }
        return render(request, 'movies/recommended.html', context)