from django.urls import path
from . import views
from .views import CustomAuthToken

urlpatterns = [
    path('movieList/', views.movieList, name="movieList"),
    path('topFeatured', views.topFeatured, name="topFeatured"),
    # path('example_view', views.example_view, name="example_view"),
    path('login', CustomAuthToken.as_view())
]
