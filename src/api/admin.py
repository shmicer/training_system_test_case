from django.contrib import admin

from .models import Lesson, Product, ProductAccess

admin.site.register(Lesson)
admin.site.register(Product)
admin.site.register(ProductAccess)
