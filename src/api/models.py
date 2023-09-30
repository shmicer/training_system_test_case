from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    lessons = models.ManyToManyField('Lesson', related_name='products')

    class Meta:
        unique_together = ['name', 'owner']


class ProductAccess(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField(blank=True)
    video_link = models.URLField()
    duration = models.IntegerField(null=False)


class LessonView(models.Model):
    last_view = models.DateTimeField(auto_now=True)
    viewed_seconds = models.IntegerField(default=0)
    is_viewed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
