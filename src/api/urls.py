from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LessonViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('api/', include(router.urls)),
]
