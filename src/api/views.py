
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import LessonView, Product, Lesson
from .permissions import HasAccessToLesson, IsOwnerOrReadOnly
from .serializers import (LessonViewSerializer, ProductSerializer,
                          LessonListSerializer)


class LessonViewSet(viewsets.ModelViewSet):
    """
    Return a queryset of all lessons for authenticated user with a status of view.
    """
    queryset = LessonView.objects.all().select_related('lesson', 'product')
    serializer_class = LessonListSerializer
    permission_classes = [permissions.IsAuthenticated, HasAccessToLesson]


class ProductViewSet(viewsets.ViewSet):

    """
    Return a queryset of all products for authenticated
    user and retrieve product info such as status,
    view time and the last view date of lesson.
    """
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly, ]


    def list(self, request, *args, **kwargs):
        queryset = Product.objects.filter(productaccess__user=self.request.user)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        product = Product.objects.get(pk=pk)
        lessons = LessonView.objects.filter(user=self.request.user, product=product).select_related('lesson')
        serializer = LessonViewSerializer(lessons, many=True)
        return Response(serializer.data)
