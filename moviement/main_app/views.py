from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import TakeForm

# Create your views here.

def home (request):
    return render(request, 'home.html')

def movies_index (request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html',{
        'movies': movies
    })

def take_create (request, movie_id):
    form = TakeForm
    return render(request, 'movies/take_create.html',{
        'form': form,
        'movie_id': movie_id
    })


def take_add(request, movie_id):
    form = TakeForm(request.POST)
    if form.is_valid():
        new_take = form.save(commit=False)
        new_take.movie_id = movie_id
        new_take.save()
    return redirect('detail', pk=movie_id)


class MovieDetail (DetailView):
    model = Movie
    template_name = "movies/detail.html"