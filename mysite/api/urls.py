from django.urls import path
from . import views
from .views import CustomAuthToken

urlpatterns = [
    path('movieList/', views.movieList, name="movieList"),
    path('detail/<str:pk>/', views.movieDetails, name="detail"),
    path('search/<str:find>/', views.movieFilter, name="search"),
    path('create', views.createNewMovie, name="create"),
    path('update/<str:pk>/', views.updateMovie, name="update"),
    path('delete/<str:pk>/', views.deleteMovie, name="delete"),
    path('topFeatured', views.topFeatured, name="topFeatured"),
    # path('example_view', views.example_view, name="example_view"),
    path('login', CustomAuthToken.as_view())
]
