from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


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
    products = models.ManyToManyField(Product)

class LessonView(models.Model):
    last_view = models.DateTimeField(auto_now=True)
    viewed_seconds = models.IntegerField(default=0)
    is_viewed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def update_view_status(self):
        total_seconds = self.lesson.duration
        if self.viewed_seconds >= 0.8 * total_seconds:
            self.is_viewed = True
        else:
            self.is_viewed = False

    def save(self, *args, **kwargs):
        self.update_view_status()
        super().save(*args, **kwargs)



