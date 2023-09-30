from rest_framework import serializers
from .models import Product, Lesson, LessonView, ProductAccess


class LessonViewSerializer(serializers.ModelSerializer):
    lesson_name = serializers.ReadOnlyField(source='lesson.name')

    class Meta:
        model = LessonView
        fields = ['lesson_name', 'last_view', 'viewed_seconds', 'is_viewed']


class LessonSerializer(serializers.ModelSerializer):
    lessonview_set = LessonViewSerializer(many=True, read_only=True)


    class Meta:
        model = Lesson
        fields = ['lessonview_set']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name']


class ProductViewSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'lessons']








