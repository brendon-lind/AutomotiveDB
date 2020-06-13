from django.urls import include, path
from rest_framework import routers

from .viewsets import CustomerViewSet, CommentViewSet, CarViewSet, CarFileViewSet

router = routers.DefaultRouter()
router.register('car_files', CarFileViewSet)
router.register('customers', CustomerViewSet)
router.register('cars', CarViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
