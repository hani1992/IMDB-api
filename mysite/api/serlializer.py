from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# class UserSerializaer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = {'id', 'username', 'email'}

# class LoginSerializer(serializers.Serializer):
    # username = serializers.CharField()
    # password = serializers.CharField()
    #
    # def validate(self, data):
    #     user = authenticate(**data)
    #     if user and user.is_active:
    #         return user
    #     raise serializers.ValidationError("Incorrect Credintials")

class MovieSerializer(serializers.ModelSerializer):
    tag = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Movies
        fields = '__all__'

