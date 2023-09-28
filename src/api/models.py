from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Access(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.URLField()
    products = models.ManyToManyField(Product)
    duration = models.IntegerField()

class LessonView(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    duration_view = models.IntegerField()
    is_viewed = models.BooleanField(default=False)