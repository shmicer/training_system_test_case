
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import LessonView, Product
from .permissions import HasAccessToLesson, IsOwnerOrReadOnly
from .serializers import (LessonViewSerializer, ProductSerializer,
                          ProductViewSerializer)


class LessonViewSet(viewsets.ModelViewSet):
    """
    Return a queryset of all lessons for authenticated user with a status of view.
    """
    queryset = LessonView.objects.all().select_related('lesson')
    serializer_class = LessonViewSerializer
    permission_classes = [permissions.IsAuthenticated, HasAccessToLesson]


class ProductViewSet(viewsets.ModelViewSet):
    """
    Return a queryset of all products for authenticated
    user and retrieve product info such as status,
    view time and the last view date of lesson.
    """
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly, ]

    def get_queryset(self):
        return (Product.objects.filter(productaccess__user=self.request.user)
                .prefetch_related('lessons__lessonview_set'))

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_queryset()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductViewSerializer(product)
        return Response(serializer.data)
