from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path("admin/", admin.site.urls),
    path('', include('api.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
