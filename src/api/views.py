
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .permissions import HasAccessToLesson, HasAccessToProduct, IsOwnerOrReadOnly
from .serializers import LessonViewSerializer, ProductSerializer
from .models import LessonView, Product, ProductAccess


class LessonViewSet(viewsets.ModelViewSet):
    """
    Return a queryset of all lessons for given user with a status of view.
    """
    queryset = LessonView.objects.all().select_related('lesson')
    serializer_class = LessonViewSerializer
    permission_classes = [ permissions.IsAuthenticated, HasAccessToLesson]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().prefetch_related('lessons__lessonview_set')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly, HasAccessToProduct]









