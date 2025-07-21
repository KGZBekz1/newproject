from rest_framework import serializers
from .models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '_all_'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '_all_'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '_all_'