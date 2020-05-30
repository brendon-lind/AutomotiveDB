from rest_framework import serializers

from .models import Customer, Comment, Car


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id',
            'name',
            'phone_number',
            'description',
            'portrait',
        )


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id',
            'customer',
            'year',
            'model',
            'vin',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'content',
            'date_created',
            'date_updated',
        )
