from rest_framework import viewsets, mixins

from .serializers import CustomerSerializer, CarSerializer, CarFileSerializer, CommentSerializer
from .models import Customer, CarFile, Car, Comment
from .filtersets import CommentFilterSet


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CarFileViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CarFile.objects.all()
    serializer_class = CarFileSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_class = CommentFilterSet

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('-date_created')
