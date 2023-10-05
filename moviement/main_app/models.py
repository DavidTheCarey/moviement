from django.db import models
from django.contrib.auth.models import User


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
    rating = models.IntegerField()
    # user_likes
    description = models.TextField(max_length=3000)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title