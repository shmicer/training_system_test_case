from django.db.models import Count, Q, Sum
from drf_spectacular.utils import extend_schema
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import LessonView, Product, ProductAccess
from .permissions import IsOwnerOrReadOnly
from .serializers import (LessonListSerializer, LessonViewSerializer,
                          ProductSerializer, ProductSummarySerializer)


@extend_schema(
    summary='Return a list of all lessons for authenticated user with a status of view',
)
class LessonViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = (LessonView.objects
                    .filter(user=self.request.user)
                    .select_related('lesson', 'product'))
        serializer = LessonListSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly, ]

    @extend_schema(
        summary='Return a list of all products for authenticated user',
    )
    def list(self, request, *args, **kwargs):
        queryset = Product.objects.filter(productaccess__user=self.request.user)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        summary='Retrieve product lessons list with status, view time and the last view date of lesson',
    )
    def retrieve(self, request, pk=None, *args, **kwargs):
        product = Product.objects.get(pk=pk)
        lessons = (LessonView.objects
                   .filter(user=self.request.user, product=product)
                   .select_related('lesson'))
        serializer = LessonViewSerializer(lessons, many=True)
        return Response(serializer.data)


@extend_schema(
    summary='Get product summary',
    description='Get a detail product information such as number of users,'
                'total viewed lessons,total time of view in seconds, '
                'percentage of buying this product'
)
class ProductSummaryViewSet(viewsets.ViewSet):
    serializer_class = ProductSummarySerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, pk=None, *args, **kwargs):
        viewed_filter = Q(lessons__lessonview__is_viewed=True)
        product = Product.objects.filter(owner=self.request.user).annotate(
            number_of_users=Count('productaccess__user', distinct=True),
            total_lessons_viewed=Count('lessons__lessonview', filter=viewed_filter, distinct=True),
            total_time_viewed=Sum('lessons__lessonview__viewed_seconds', filter=viewed_filter),
        ).get(pk=pk)

        total_user_count = ProductAccess.objects.all().values('user').distinct().count()
        product.buy_percentage = (
            int(100 * (product.number_of_users / total_user_count))) \
            if total_user_count != 0 else 0
        serializer = ProductSummarySerializer(product)
        return Response(serializer.data)
