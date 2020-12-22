from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serlializer import *

# Create your views here.

@api_view(['GET'])
def movieList(request):
    movies = Movies.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def topRates(request):
    movies = Movies.objects.values_list('id', 'title', 'tag__name')
    print(movies)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def topFeatured(request):
    movies = Movies.objects.filter(IsFeatured=True)
    print(movies)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
