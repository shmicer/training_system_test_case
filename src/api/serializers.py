from rest_framework import serializers

from .models import Lesson, LessonView, Product


class LessonViewSerializer(serializers.ModelSerializer):
    lesson_name = serializers.ReadOnlyField(source='lesson.name')

    class Meta:
        model = LessonView
        fields = ['lesson_name', 'last_view', 'viewed_seconds', 'is_viewed']

class LessonListSerializer(serializers.ModelSerializer):
    lesson_name = serializers.ReadOnlyField(source='lesson.name')
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = LessonView
        fields = ['product_name', 'lesson_name', 'last_view', 'viewed_seconds', 'is_viewed']

class LessonSerializer(serializers.ModelSerializer):
    lessonview_set = LessonViewSerializer(many=True, read_only=True)


    class Meta:
        model = Lesson
        fields = ['lessonview_set', ]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name']


class ProductViewSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'lessons']


class ProductSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', '']
