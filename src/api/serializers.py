from rest_framework import serializers
from .models import Product, Lesson, LessonView, ProductAccess


class LessonViewSerializer(serializers.ModelSerializer):
    lesson_name = serializers.ReadOnlyField(source='lesson.name')
    is_viewed = serializers.SerializerMethodField()

    class Meta:
        model = LessonView
        fields = ['lesson_name', 'last_view', 'viewed_seconds', 'is_viewed']

    def get_is_viewed(self, obj):
        return obj.viewed_seconds >= 0.8 * obj.lesson.duration


class LessonSerializer(serializers.ModelSerializer):
    lessonview_set = LessonViewSerializer(many=True, read_only=True)
    class Meta:
        model = Lesson
        fields = ['name', 'duration', 'lessonview_set']


class ProductSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'owner', 'lessons']








