from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImageUploadViewSet

router = DefaultRouter()
router.register(r'upload', ImageUploadViewSet, basename='image-upload')

urlpatterns = [
    path('', include(router.urls)),
]