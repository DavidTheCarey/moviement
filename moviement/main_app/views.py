import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import TakeForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home (request):
    return render(request, 'home.html')

def movies_index (request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html',{
        'movies': movies
    })

@login_required
def take_create (request, movie_id):
    form = TakeForm
    return render(request, 'movies/take_create.html',{
        'form': form,
        'movie_id': movie_id
    })

@login_required
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
        "current_user": user,
        "takes": takes
    })
    
class DeleteTake(DeleteView, LoginRequiredMixin):
    model = Take
    template_name = 'movies/take_confirm_delete.html'
    success_url = '/movies/'

# def take_update(request, take_id):
#     form = TakeForm
#     return render(request, 'movies/take_create.html',{
#         'form': form,
#         'take_id': take_id
#     })

class TakeUpdate(UpdateView, LoginRequiredMixin):
   model = Take
   fields = ["title","themes","rating","description"]
   template_name = 'movies/take_create.html'

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["take_id"] = self.kwargs['pk']
        return context

def add_photo(request, take_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    movie_id = request.POST["movie"]
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Shot.objects.create(url=url, take_id=take_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', movie_id)