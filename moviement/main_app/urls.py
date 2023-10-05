from . import views
from django.urls import path
urlpatterns = [
    path("", views.home, name="home"),
    path("movies/", views.movies_index, name="index"),
    path("movies/<int:pk>", views.MovieDetail.as_view(), name="detail"),
    path("movies/<int:movie_id>/take/create", views.take_create, name="take_create"),
    path("movies/<int:movie_id>/take/add", views.take_add, name="take_add"),
    path("profile/", views.profile, name="profile"),
    path("profile/<int:user_id>", views.profile, name="user_profile"),
    path('profile/signup/', views.signup, name='signup'),
]
