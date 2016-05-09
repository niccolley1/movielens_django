from django.http import HttpResponse
from .models import Movie, Critic, Review
from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'movies/index.html', {'all_movies': Movie.objects.all()})


def detail(request, movie_id):
    all_movies = get_object_or_404(Movie, id=movie_id)
    movies_reviewed = Review.objects.filter(movie=movie_id)
    return render(request, 'movies/detail.html', {'movie': all_movies, 'reviewed': movies_reviewed})


def critic(request, critic_id):
    all_critics = get_object_or_404(Critic, id=critic_id)
    movies_reviewed = Review.objects.filter(critic=critic_id)
    return render(request, 'movies/critic.html',
                  {'critic': all_critics,
                   'reviewed': movies_reviewed})


def top(request, num=20):
    top_n = Movie.get_top(num)
    top_movies = {'top': top_n}
    return (request, 'movies/top', top_movies)
