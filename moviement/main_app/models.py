from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    review_score = models.IntegerField()
    # user_favs = ManyToManyField(User)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class Take(models.Model):
    title = models.CharField(max_length=250)
    themes = models.CharField(max_length=250)
    rating = models.IntegerField(validators=[MaxValueValidator(10)])
    # user_likes
    description = models.TextField(max_length=3000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.movie.id})

class Shot(models.Model):
    url = models.CharField(max_length=200)
    take = models.ForeignKey(Take, on_delete=models.CASCADE)

    def __str__(self):
        return f"Shot: {self.id}, Take: {self.take_id} @{self.url}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fav_movies = models.ManyToManyField(Movie)
    
    def __str__(self):
        return f"{self.user.username}"
