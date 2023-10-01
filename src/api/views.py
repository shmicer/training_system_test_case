from django.db.models import Count, Sum, Q
from django.db.models.functions import Coalesce
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import LessonView, Product, Lesson, ProductAccess
from .permissions import HasAccessToLesson, IsOwnerOrReadOnly
from .serializers import (LessonViewSerializer, ProductSerializer,
                          LessonListSerializer, ProductSummarySerializer)


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


class ProductSummaryViewSet(viewsets.ViewSet):
    serializer_class = ProductSummarySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly, ]

    def retrieve(self, request, pk=None, *args, **kwargs):
        viewed_filter = Q(lessons__lessonview__is_viewed=True)
        product = Product.objects.annotate(
            number_of_users=Count('productaccess__user', distinct=True),
            total_lessons_viewed=Count('lessons__lessonview', filter=viewed_filter, distinct=True),
            total_time_viewed=Sum('lessons__lessonview__viewed_seconds', filter=viewed_filter),
        ).get(pk=pk)

        total_user_count = ProductAccess.objects.all().values('user').distinct().count()
        product.buy_percentage = int(100 * (product.number_of_users / total_user_count)) if total_user_count != 0 else 0

        serializer = ProductSummarySerializer(product)
        return Response(serializer.data)


