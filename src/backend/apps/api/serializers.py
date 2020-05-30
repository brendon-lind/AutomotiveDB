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
    customer_name = serializers.SerializerMethodField(read_only=True)
    customer_phone_number = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Car
        fields = (
            'id',
            'customer_name',
            'customer_phone_number',
            'year',
            'model',
            'vin',
        )

    def get_customer_name(self, obj):
        return obj.customer.name

    def get_customer_phone_number(self, obj):
        return obj.customer.phone_number


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'content',
            'date_created',
            'date_updated',
        )
