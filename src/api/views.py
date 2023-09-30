
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .permissions import HasAccessToLesson
from .serializers import  LessonSerializer, LessonViewSerializer
from .models import Lesson, LessonView


class LessonViewSet(viewsets.ModelViewSet):
    queryset = LessonView.objects.all()
    serializer_class = LessonViewSerializer
    permission_classes = [ permissions.IsAuthenticated, HasAccessToLesson]


    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     data  = [i for i in serializer.data]
    #     return Response(data)








