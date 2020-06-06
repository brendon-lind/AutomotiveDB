from rest_framework import serializers

from .models import Customer, Comment, Car, CarFile


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


class CarFileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CarFile
        fields = (
            'id',
            'car',
            'file',
            'type',
            'name',
        )

    def get_name(self, obj):
        return obj.file.name


class CarSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField(read_only=True)
    customer_phone_number = serializers.SerializerMethodField(read_only=True)
    make_and_model = serializers.SerializerMethodField(read_only=True)

    files = CarFileSerializer(read_only=True, many=True)

    class Meta:
        model = Car
        fields = (
            'id',
            'customer',
            'customer_name',
            'customer_phone_number',
            'make_and_model',
            'year',
            'make',
            'model',
            'vin',
            'engine_size',
            'engine_layout',
            'fuel',
            'header_photo',
            'files',
        )

    def get_customer_name(self, obj):
        return obj.customer.name

    def get_customer_phone_number(self, obj):
        return obj.customer.phone_number

    def get_make_and_model(self, obj):
        return f'{obj.make} {obj.model}'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'car',
            'content',
            'date_created',
            'date_updated',
        )
