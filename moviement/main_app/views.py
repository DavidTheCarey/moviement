from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import TakeForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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
        new_take.user = request.user
        new_take.save()
    return redirect('detail', pk=movie_id)


class MovieDetail (DetailView):
    model = Movie
    template_name = "movies/detail.html"

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def profile(request, user_id=0):
    id = request.user.id if not user_id else user_id
    user = User.objects.get(id=id)
    takes = Take.objects.filter(user_id=id)
    return render(request, 'registration/profile.html', {
        "user": user,
        "takes": takes
    })

