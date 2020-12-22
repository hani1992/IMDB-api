from rest_framework import serializers
from .models import *


class MovieSerializer(serializers.ModelSerializer):
    tag = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Movies
        fields = '__all__'

