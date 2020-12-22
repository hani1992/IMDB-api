from django.urls import path
from . import views

urlpatterns = [
    path('movieList/', views.movieList, name="movieList"),
    path('topFeatured', views.topFeatured, name="topFeatured")
]
