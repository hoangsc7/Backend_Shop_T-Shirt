from rest_framework import serializers

from .models import Product,Category

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'description',
            'price',
            'get_image',
            'get_thumbnail',
        )

class categorySerializer(serializers.ModelSerializer):
    products = productSerializer(many=True) 
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'products',
        )