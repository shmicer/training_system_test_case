from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Lesson


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', '']