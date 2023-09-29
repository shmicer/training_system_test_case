from rest_framework import serializers
from django.contrib.auth.models import User


from .models import Product, Lesson, LessonView


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'owner']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'duration_view', 'is_viewed']


class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = ['id', 'lesson', 'viewed_seconds', 'is_viewed']



