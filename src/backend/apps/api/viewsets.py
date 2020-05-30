from rest_framework import viewsets

from .serializers import CustomerSerializer, CarSerializer, CommentSerializer
from .models import Customer, Car, Comment
from .filtersets import CommentFilterSet


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


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
